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
| **IDs**<br/>`AutoField`, `BigAutoField` | `IdFilterInput` | `exact`, `in`, `gt`, `gte`, `lt`, `lte`, `isnull` |
| **Foreign Keys & One-to-One Relations**<br/>`ForeignKey`, `OneToOneField` | `Generic_<Model>FilterInput` *(depth-controlled)* | All fields of the related model (e.g. `party.abbreviation`, `party.partyname`, `party.id`) plus `isnull` |
| **Decimals & Floats**<br/>`FloatField`, `DecimalField` | `FloatFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `range`, `isnull` |
| **Dates**<br/>`DateField` | `DateFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `range`, `year`, `month`, `day`, `isnull` |
| **Date & Time**<br/>`DateTimeField` | `DateTimeFilterInput` | `exact`, `gt`, `gte`, `lt`, `lte`, `range`, `date`, `year`, `month`, `day`, `isnull` |
| **Booleans**<br/>`BooleanField`, `NullBooleanField` | `BooleanFilterInput` | `exact`, `isnull` |

### 🔗 Foreign Key Relational Filtering Example

You can filter records based on related model fields (e.g. filtering Chief Ministers by party abbreviation or state name):

```graphql
query {
  allCms(
    filters: {
      party: {
        abbreviation: {
          startswith: "BJ"
          exact: "BJP"
        }
        partyname: {
          icontains: "Janata"
        }
        isnull: false
      }
      rulingstate: {
        Statename: {
          exact: "Andhra Pradesh"
        }
      }
    }
    limit: 10
  ) {
    total
    data {
      id
      name
      party {
        abbreviation
        partyname
      }
      rulingstate {
        Statename
      }
    }
  }
}
```

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

---

## 🔬 Schema Introspection & Discovery Guide

GraphQL provides a built-in introspection system via `__type` and `__schema` to discover queries, mutations, filter inputs, and output fields.

### ⚠️ Common Pitfall: Introspecting Root `Query` vs. Specific Models

When running an introspection query on `__type(name: "Query")`:
```graphql
query IntrospectAllCms {
  __type(name: "Query") {
    fields {
      name
      type { name kind }
    }
  }
}
```
- The operation name `IntrospectAllCms` is just a client-side label; **it does not filter GraphQL introspection results**.
- `__type(name: "Query")` inspects the root `Query` type, which aggregates **all** query classes (`GenericQuery`, `EnumQuery`, `governorQuery`, `cmQuery`, `loksabhaQuery`).
- Therefore, the returned `fields` array contains every query across all modules in the project (e.g. `allPartys`, `allCms`, `allGovernors`, `lokSabhaMpsTable`, `allCmsTable`, etc.).

To inspect a **specific model's filters or output fields**, query its specific type name directly using the naming conventions below.

---

### 🏷️ Type Naming Conventions Cheatsheet

| Purpose | Naming Pattern | Examples |
| :--- | :--- | :--- |
| **Model Output Type** | `Generic_<app_label>_<ModelName>Type` | `Generic_party_PartyType`, `Generic_cm_cmType`, `Generic_state_StateType` |
| **Paginated List Type** | `Generic_<app_label>_<ModelName>PaginatedType` | `Generic_party_PartyPaginatedType`, `Generic_cm_cmPaginatedType` |
| **Filter Input Type** | `Generic_<app_label>_<ModelName>FilterInput` | `Generic_party_PartyFilterInput`, `Generic_cm_cmFilterInput` |
| **Create Input Type** | `Create<ModelName>Input` | `CreatePartyInput`, `CreateCmInput` |
| **Update Input Type** | `Update<ModelName>Input` | `UpdatePartyInput`, `UpdateCmInput` |
| **Mutation Payload** | `Generic_<app_label>_<ModelName>Payload` | `Generic_party_PartyPayload`, `Generic_cm_cmPayload` |

---

### 1. Discover Available Filters for a Model (Input Fields & Operators)

To find all filterable fields and their nested operator types on any model (e.g., `cm` or `Party`):

```graphql
query GetCmFilterFields {
  __type(name: "Generic_cm_cmFilterInput") {
    name
    description
    inputFields {
      name
      description
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
```

#### Discover Operators for a Specific Data Type:
To see all available operators (e.g., `exact`, `icontains`, `in`, `gt`, `range`, `isnull`) on an operator filter type:

```graphql
query GetStringFilterOperators {
  __type(name: "StringFilterInput") {
    name
    description
    inputFields {
      name
      description
      type {
        name
        kind
      }
    }
  }
}
```
*(You can also inspect `IntFilterInput`, `DateFilterInput`, `DateTimeFilterInput`, `FloatFilterInput`, `IdFilterInput`, `BooleanFilterInput`)*.

---

### 2. Discover Output Fields & Return Values (Output Types)

#### A. Discover Paginated Query Output Structure (`total`, `offset`, `limit`, `data`):
```graphql
query GetCmPaginationOutput {
  __type(name: "Generic_cm_cmPaginatedType") {
    name
    fields {
      name
      description
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
```

#### B. Discover Model Fields Available Inside `data { ... }`:
To find every scalar column and relationship field you can select on the model:

```graphql
query GetCmModelOutputFields {
  __type(name: "Generic_cm_cmType") {
    name
    fields {
      name
      description
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
```

#### C. Discover Legacy / Custom Table Output Types (e.g., `TableCmType`, `TableLoksabhaType`):
```graphql
query GetTableCmOutputFields {
  __type(name: "TableCmType") {
    name
    fields {
      name
      type {
        name
        kind
      }
    }
  }
}
```

---

### 3. Discover Mutation Arguments & Payloads

#### A. Discover Input Fields for Create / Update:
```graphql
query GetCreatePartyInputFields {
  __type(name: "CreatePartyInput") {
    name
    inputFields {
      name
      description
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
```

#### B. Discover Mutation Response Payload Fields:
```graphql
query GetPartyMutationPayload {
  __type(name: "Generic_party_PartyPayload") {
    name
    fields {
      name
      type {
        name
        kind
        ofType {
          name
          kind
        }
      }
    }
  }
}
```

---

### 4. Comprehensive Query Field Inspection

To inspect a top-level query (such as `allPartys` or `allCms`) along with all its arguments and output structure in a single query:

```graphql
query IntrospectAllQueriesAndArgs {
  __schema {
    queryType {
      fields {
        name
        description
        args {
          name
          defaultValue
          type {
            name
            kind
            ofType {
              name
              kind
            }
          }
        }
        type {
          name
          kind
          ofType {
            name
            kind
            fields {
              name
              type {
                name
                kind
              }
            }
          }
        }
      }
    }
  }
}
```
*(Filter the returned `fields` list in your client by `name === "allPartys"` or `name === "allCms"`)*.


