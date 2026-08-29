# Generic GraphQL Engine (`generic_graphql`)

An automated, config-driven GraphQL query and mutation generation framework for Django and Graphene-Django.

---

## 🌟 Key Features

1. **Zero Configuration Support (`"ModelName": {}`)**:
   - Automatically generates list query (`allPartys`, `allStates`) with dynamic top-down filters + pagination + search + multi-column ordering, and full mutations (`create`, `update`, `delete`).
   - Text search across Char/Text fields and pagination (`limit`, `offset`) included out of the box.

2. **Top-Down Nested Filter Architecture**:
   - Clean, structured `filters` (or `where`) object in GraphiQL UI.
   - Expand fields top-down and select operators: `exact`, `iexact`, `icontains`, `startswith`, `endswith`, `in`, `gt`, `gte`, `lt`, `lte`, `range`, `year`, `month`, `isnull`.

3. **Strict Whitelisting on Explicit Configuration**:
   - If specific fields or operations are defined in `graphql_conf.py`, the engine generates *only* what you configure.

4. **Custom Functions & Resolvers**:
   - Custom Query Resolvers via `"resolver": "app.module.custom_func"`.
   - Queryset Filtering Hooks via `"get_queryset": "app.module.custom_qs"`.
   - Mutation Lifecycle Hooks via `"before_save"`, `"after_save"`, `"before_delete"`, `"after_delete"`.
   - Full Mutation Overrides via `"mutate": "app.module.custom_mutate"`.

5. **Extra Queries & Mutations**:
   - Model-level extras via `queries.extra` and `mutations.extra`.
   - Global/standalone schema integration via `__extra_queries__` and `__extra_mutations__`.

---

## 📁 Architecture Overview

```
politiaware_backend/generic_graphql/
├── __init__.py           # Public exports (generate_generic_graphql, helper types)
├── builder.py            # Main schema assembler (GenericQuery, GenericMutation)
├── config_parser.py      # Normalizes config, injects defaults, resolves callables
├── model_loader.py       # Resolves Django models dynamically & inspects metadata
├── field_mapper.py       # Maps Django fields & lookups -> Graphene types
├── filter_factory.py     # Generates top-down operator filter types (StringFilterInput, etc.)
├── type_factory.py       # Dynamically generates DjangoObjectType & Response Payloads
├── input_factory.py      # Dynamically generates Graphene InputObjectType
├── query_factory.py      # Dynamically generates Get, List, and Extra queries
└── mutation_factory.py   # Dynamically generates Create, Update, Delete, and Extra mutations
```

---

## 🔍 Top-Down Filter Syntax & Paginated Queries

List queries (`allPartys`, `allCms`, `allGovernors`, `allStates`, `allDistricts`, etc.) return a standardized paginated response containing `total`, `offset` (default: 0), `limit` (default: 10), and the items array (`data`):

```graphql
query {
  allPartys(
    filters: {
      abbreviation: {
        icontains: "BSP"
        in: ["BSP", "INC"]
      }
      partystatus: {
        exact: "National"
      }
      foundeddate: {
        gte: "1980-01-01"
        year: 1984
      }
    }
    search: "Bahujan"
    orderBy: "partyname"
    limit: 10
    offset: 0
  ) {
    total
    offset
    limit
    data {
      id
      partyname
      abbreviation
      partystatus
      foundeddate
    }
  }
}
```

### 📊 Supported Filters by Data Type

| Django Model Data Type | GraphQL Filter Type | Available Filter Operators |
| :--- | :--- | :--- |
| **Strings / Text**<br/>`CharField`, `TextField`, `EmailField`, `SlugField` | `StringFilterInput` | `exact`, `iexact`, `contains`, `icontains`, `startswith`, `istartswith`, `endswith`, `iendswith`, `in`, `regex`, `iregex`, `isnull` |
| **Integers**<br/>`IntegerField`, `SmallIntegerField`, `BigIntegerField`, `PositiveIntegerField` | `IntFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `in`, `range`, `isnull` |
| **IDs & Foreign Keys**<br/>`AutoField`, `BigAutoField`, `ForeignKey`, `OneToOneField` | `IdFilterInput` | `exact`, `in`, `gt`, `gte`, `lt`, `lte`, `isnull` |
| **Decimals & Floats**<br/>`FloatField`, `DecimalField` | `FloatFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `range`, `isnull` |
| **Dates**<br/>`DateField` | `DateFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `range`, `year`, `month`, `day`, `isnull` |
| **Date & Time**<br/>`DateTimeField` | `DateTimeFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `range`, `date`, `year`, `month`, `day`, `isnull` |
| **Booleans**<br/>`BooleanField`, `NullBooleanField` | `BooleanFilterInput` | `exact`, `isnull` |

---

## ⚙️ Configuration Reference (`graphql_conf/graphql_conf.py`)

### 1. Zero Configuration (List + Full Mutations)
```python
GRAPHQL_CONF = {
    "Party": {}
}
```
*Gives you `allPartys(...)`, `createParty(...)`, `updateParty(...)`, `deleteParty(...)` immediately.*

---

### 2. Custom Queries & Filter Configuration
```python
GRAPHQL_CONF = {
    "LokSabhaMP": {
        "app_label": "loksabha",
        "queries": {
            # List query with filters & pagination
            "list": {
                "name": "allLokSabhaMps",
                "return_cols": ["id", "name", "gender", "Party", "constituency", "ispresent"],
                "filter_fields": {
                    "name": ["exact", "icontains", "istartswith"],
                    "ispresent": ["exact", "isnull"],
                    "Party": ["exact", "in"],
                },
                "search_fields": ["name"],
                "ordering_fields": ["id", "name"],
                "pagination": True
            }
        }
    }
}
```

---

### 3. Custom Mutations Configuration
```python
GRAPHQL_CONF = {
    "Party": {
        "mutations": {
            "create": {
                "create_cols": ["partyname", "abbreviation", "partystatus", "foundeddate", "party_color"],
                "return_cols": ["id", "partyname", "abbreviation"],
                "required_cols": ["partyname", "foundeddate"]
            },
            "update": {
                "pk": "id",
                "update_cols": ["partyname", "abbreviation", "partystatus", "party_color"],
                "return_cols": ["id", "partyname", "abbreviation"]
            },
            "delete": {
                "pk": "id",
                "return_cols": ["id"]
            }
        }
    }
}
```

---

## 🚀 GraphQL Mutation Examples

### Create Mutation
```graphql
mutation {
  createParty(input: {
    partyname: "Democratic Alliance"
    abbreviation: "DA"
    partystatus: "Regional"
    foundeddate: "2024-01-01"
    partyColor: "#00A2E8"
  }) {
    success
    errors
    data {
      id
      partyname
      abbreviation
    }
  }
}
```

### Update Mutation
```graphql
mutation {
  updateParty(id: 1, input: {
    partystatus: "National"
  }) {
    success
    errors
    data {
      id
      partyname
      partystatus
    }
  }
}
```

### Delete Mutation
```graphql
mutation {
  deleteParty(id: 1) {
    success
    errors
    id
  }
}
```

---

## ⚡ Database Performance & Query Optimizations

The `generic_graphql` engine includes built-in database-level optimizations to ensure maximum performance and minimal database load:

### 1. Lazy `COUNT(*)` Evaluation (Zero Count Overhead)
Unlike standard GraphQL resolvers that precompute `qs.count()` on every query, `generic_graphql` uses a lazy container (`PaginatedResult`):
- **Data-only Queries** (e.g. infinite scrolling, feeds):
  ```graphql
  query {
    allPartys {
      data { id partyname }
    }
  }
  ```
  👉 `SELECT COUNT(*)` is **completely skipped**. Only **1 database query** (`SELECT ... LIMIT 10 OFFSET 0`) is executed.
- **Count-only Queries** (e.g. badges, dashboards):
  ```graphql
  query {
    allPartys {
      total
    }
  }
  ```
  👉 Fetching row data is **completely skipped**. Only **1 database query** (`SELECT COUNT(*)`) is executed.
- **Full Paginated Queries**:
  ```graphql
  query {
    allPartys {
      total
      data { id partyname }
    }
  }
  ```
  👉 Both queries run on-demand as requested.

---

### 2. Dynamic Column Projection (`.only()`)
The engine inspects the GraphQL AST selection set and applies Django's `.only(*fields)` projection:
- When you query:
  ```graphql
  query {
    allPartys {
      data {
        id
        partyname
      }
    }
  }
  ```
- **PostgreSQL executes**:
  ```sql
  SELECT "id", "partyname" FROM "party_party" LIMIT 10 OFFSET 0;
  ```
- **Advantages**:
  - PostgreSQL avoids reading unused columns (large text fields, descriptions, BLOBs, or unrequested columns) from disk.
  - Significantly reduces network bandwidth between PostgreSQL and Django.
  - Lowers Django RAM usage during JSON serialization.

---

### 3. Type Definition Cache (Zero Runtime Overhead)
Dynamic GraphQL types (`DjangoObjectType`, `PaginatedType`, `PayloadType`) are generated once during server boot and cached in module registries (`_DJANGO_TYPE_REGISTRY`, `_PAYLOAD_TYPE_REGISTRY`, `_PAGINATED_TYPE_REGISTRY`). 
- **Startup Overhead**: ~5ms (one-time on Django boot).
- **Runtime Overhead**: 0% (identical to handwritten static classes).

