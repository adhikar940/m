"""
GraphQL configuration per model for generic_graphql.

Behavior:
1. Zero Configuration ("ModelName": {}):
   - Automatically generates list query (e.g. allPartys, allStates) with all data-type filters + pagination + search + ordering, and full mutations (create, update, delete).
2. Explicit Configuration:
   - Whitelists only the specified operations and fields.
3. Custom Functions:
   - Use 'resolver', 'get_queryset', 'before_save', 'after_save', or 'mutate' to override or hook into logic.
4. Extra Queries & Mutations:
   - Use 'queries.extra' and 'mutations.extra' to add extra domain-specific queries and mutations.
"""

GRAPHQL_CONF = {
    "Party": {},  # Zero config - full CRUD
    "cm": {},
    "governor": {},
    "State": {},
    "District": {},
}