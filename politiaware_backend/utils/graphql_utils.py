from django.db.models import Q

def graphql_search(base_fields, search, search_fields, search_mode, queryset):
    """
    search --  list of search terms
    search_fields -- list of Enum or string field names
    search_mode -- 'contains' or 'exact'
    """
    lookup = "__iexact" if (getattr(search_mode, "value", search_mode) == "exact") else "__icontains"

    # Prepare search field lookups
    all_search_fields = {
        key: value + lookup
        for key, value in base_fields.items()
    }

    if search:
        fields = [getattr(f, "value", f) for f in (search_fields or all_search_fields.keys())]
        q_objects = Q()
        for search_term in search:
            for field in fields:
                if field in all_search_fields:
                    q_objects |= Q(**{all_search_fields[field]: search_term})
        queryset = queryset.filter(q_objects)
    return queryset


def graphql_orderby(queryset, order_by, order_fields_map):
    """
    order_by -- list of Enum or string field names 
    order_fields_map -- columns map to db
    """
    if order_by:
        mapped_order_by = []
        for field in order_by:
            field = getattr(field, "value", field)  # get Enum value
            descending = field.startswith("-")
            clean_field = field.lstrip("-")
            if clean_field in order_fields_map:
                orm_field = order_fields_map[clean_field]
                mapped_order_by.append("-" + orm_field if descending else orm_field)
        queryset = queryset.order_by(*mapped_order_by)
    return queryset