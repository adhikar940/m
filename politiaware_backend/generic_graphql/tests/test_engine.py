"""
Verification test script for generic_graphql.
Tests dynamic schema generation, query execution, and mutation execution.
"""

import os
import sys
import uuid
import django

# Setup Django environment
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "m.settings")
django.setup()

from m.schema import schema
from area_pop.models import State, Districts
from loksabha.models import LoksabhaConstituency


def run_tests():
    # Clean up any leftover test data from prior aborted test runs
    LoksabhaConstituency.objects.filter(LoksabhaConstituencyName__startswith="Test Constituency GQL").delete()
    State.objects.filter(Statename__startswith="Test State GQL").delete()

    print("--- 1. Testing Schema Introspection ---")
    query_fields = list(schema.graphql_schema.query_type.fields.keys())
    mutation_fields = list(schema.graphql_schema.mutation_type.fields.keys())

    print("Query fields available:", query_fields)
    print("Mutation fields available:", mutation_fields)

    # Check that generic queries exist
    assert "party" in query_fields, "Missing party get query"
    assert "allPartys" in query_fields, "Missing allPartys list query"

    # Check that generic mutations exist
    assert "createParty" in mutation_fields, "Missing createParty mutation"
    assert "updateParty" in mutation_fields, "Missing updateParty mutation"
    assert "deleteParty" in mutation_fields, "Missing deleteParty mutation"

    print("✅ All expected query and mutation fields exist in the schema!")

    print("\n--- 2. Testing List Query Execution with Top-Down Nested Filters & Pagination ---")
    query_str = """
    query {
        allPartys(
            filters: {
                abbreviation: { icontains: "BSP", in: ["BSP", "INC"] }
                partystatus: { exact: "National" }
            }
            limit: 5
            offset: 0
        ) {
            id
            partyname
            abbreviation
            partystatus
            partyColor
        }
    }
    """
    result = schema.execute(query_str)
    print("Query Errors:", result.errors)
    print("Query Data:", result.data)
    assert result.errors is None, f"Query execution failed: {result.errors}"
    assert "allPartys" in result.data
    print("✅ Top-down structured filter query executed successfully!")

    print("\n--- 3. Testing Single Item (Get) Query Execution ---")
    get_query_str = """
    query {
        party(id: 999999) {
            id
            partyname
        }
    }
    """
    result = schema.execute(get_query_str)
    assert result.errors is None, f"Get query failed: {result.errors}"
    print("Get Query Result (non-existent ID):", result.data)
    assert result.data["party"] is None
    print("✅ Single item (get) query executed successfully!")

    print("\n--- 4. Testing Create, Update & Delete Mutations ---")
    # Test Create Party
    create_mutation_str = """
    mutation {
        createParty(input: {
            partyname: "Test Generic Party TopDown 1"
            abbreviation: "TGPD1"
            partystatus: "Regional"
            foundeddate: "2026-01-01"
            partyColor: "#00A2E8"
            President: "President 1"
            founder: "Founder 1"
            chairperson: "Chairperson 1"
            headquarters: "HQ 1"
        }) {
            success
            errors
            party {
                id
                partyname
                abbreviation
            }
        }
    }
    """
    result = schema.execute(create_mutation_str)
    print("Create Mutation Result:", result.data, result.errors)
    assert result.errors is None, f"Create mutation error: {result.errors}"
    assert result.data["createParty"]["success"] is True
    created_id = result.data["createParty"]["party"]["id"]
    print(f"Created Party ID: {created_id}")

    # Update mutation
    update_mutation_str = f"""
    mutation {{
        updateParty(id: {created_id}, input: {{
            partystatus: "National"
        }}) {{
            success
            errors
            party {{
                id
                partystatus
            }}
        }}
    }}
    """
    upd_result = schema.execute(update_mutation_str)
    print("Update Mutation Result:", upd_result.data)
    assert upd_result.errors is None
    assert upd_result.data["updateParty"]["success"] is True

    # Delete mutation to clean up
    delete_mutation_str = f"""
    mutation {{
        deleteParty(id: {created_id}) {{
            success
            errors
            id
        }}
    }}
    """
    del_result = schema.execute(delete_mutation_str)
    print("Delete Mutation Result:", del_result.data)
    assert del_result.errors is None
    assert del_result.data["deleteParty"]["success"] is True
    print("✅ Full CRUD (Create, Update, Delete) mutations verified successfully!")

    print("\n🎉 ALL TESTS PASSED PERFECTLY!")


if __name__ == "__main__":
    run_tests()
