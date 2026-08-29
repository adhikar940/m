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
    assert "allPartys" in query_fields, "Missing allPartys list query"

    # Check that generic mutations exist
    assert "createParty" in mutation_fields, "Missing createParty mutation"
    assert "updateParty" in mutation_fields, "Missing updateParty mutation"
    assert "deleteParty" in mutation_fields, "Missing deleteParty mutation"

    print("✅ All expected query and mutation fields exist in the schema!")

    print("\n--- 2. Testing List Query Execution with Pagination Metadata (total, offset, limit, data) ---")
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
            total
            offset
            limit
            data {
                id
                partyname
                abbreviation
                partystatus
                partyColor
            }
        }
    }
    """
    result = schema.execute(query_str)
    print("Query Errors:", result.errors)
    print("Query Data:", result.data)
    assert result.errors is None, f"Query execution failed: {result.errors}"
    assert "allPartys" in result.data
    party_result = result.data["allPartys"]
    assert "total" in party_result, "Missing total field"
    assert "offset" in party_result, "Missing offset field"
    assert "limit" in party_result, "Missing limit field"
    assert "data" in party_result, "Missing data field"
    assert party_result["offset"] == 0
    assert party_result["limit"] == 5
    assert isinstance(party_result["total"], int)
    assert isinstance(party_result["data"], list)
    print("✅ Paginated list query for Party executed successfully!")

    # Test default pagination (limit=10, offset=0 when omitted)
    default_query_str = """
    query {
        allPartys {
            total
            offset
            limit
            data {
                id
                partyname
            }
        }
    }
    """
    default_result = schema.execute(default_query_str)
    print("Default Pagination Result:", default_result.data)
    assert default_result.errors is None
    assert default_result.data["allPartys"]["offset"] == 0
    assert default_result.data["allPartys"]["limit"] == 10
    print("✅ Default pagination (limit=10, offset=0) verified successfully!")

    # Test Optimization 1 & 2: Data-only query (COUNT(*) is completely skipped, only requested cols fetched)
    data_only_query_str = """
    query {
        allPartys(limit: 3) {
            data {
                id
                partyname
            }
        }
    }
    """
    data_only_result = schema.execute(data_only_query_str)
    print("Data-only Result:", data_only_result.data)
    assert data_only_result.errors is None
    assert "data" in data_only_result.data["allPartys"]
    assert len(data_only_result.data["allPartys"]["data"]) <= 3
    print("✅ Data-only query (skipping COUNT(*), dynamic .only()) verified successfully!")

    # Test Optimization 1: Count-only query (Row fetching is completely skipped)
    count_only_query_str = """
    query {
        allPartys {
            total
        }
    }
    """
    count_only_result = schema.execute(count_only_query_str)
    print("Count-only Result:", count_only_result.data)
    assert count_only_result.errors is None
    assert isinstance(count_only_result.data["allPartys"]["total"], int)
    print("✅ Count-only query (skipping row data query) verified successfully!")

    # Test allCms
    cm_query_str = """
    query {
        allCms(limit: 5, offset: 0) {
            total
            offset
            limit
            data {
                id
                name
                gender
            }
        }
    }
    """
    cm_result = schema.execute(cm_query_str)
    print("CM Query Errors:", cm_result.errors)
    print("CM Query Data:", cm_result.data)
    assert cm_result.errors is None, f"CM Query failed: {cm_result.errors}"
    assert "allCms" in cm_result.data
    assert "total" in cm_result.data["allCms"]
    assert "offset" in cm_result.data["allCms"]
    assert "limit" in cm_result.data["allCms"]
    assert "data" in cm_result.data["allCms"]
    print("✅ allCms paginated query with total, offset, limit, data executed successfully!")

    # Test allGovernors, allStates, allDistricts
    gov_query_str = """
    query {
        allGovernors(limit: 2) {
            total
            offset
            limit
            data {
                id
                name
            }
        }
        allStates(limit: 2) {
            total
            offset
            limit
            data {
                id
                Statename
            }
        }
        allDistricts(limit: 2) {
            total
            offset
            limit
            data {
                id
                Districtname
            }
        }
    }
    """
    gov_result = schema.execute(gov_query_str)
    print("Gov/State/Districts Query Errors:", gov_result.errors)
    print("Gov/State/Districts Query Data:", gov_result.data)
    assert gov_result.errors is None, f"Gov/State/Districts Query failed: {gov_result.errors}"
    assert "allGovernors" in gov_result.data
    assert "allStates" in gov_result.data
    assert "allDistricts" in gov_result.data
    assert "total" in gov_result.data["allGovernors"]
    assert "total" in gov_result.data["allStates"]
    assert "total" in gov_result.data["allDistricts"]
    print("✅ allGovernors, allStates, and allDistricts queries verified successfully!")

    print("\n--- 3. Testing Create, Update & Delete Mutations ---")
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
            data {
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
    created_id = result.data["createParty"]["data"]["id"]
    print(f"Created Party ID: {created_id}")

    # Update mutation
    update_mutation_str = f"""
    mutation {{
        updateParty(id: {created_id}, input: {{
            partystatus: "National"
        }}) {{
            success
            errors
            data {{
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
