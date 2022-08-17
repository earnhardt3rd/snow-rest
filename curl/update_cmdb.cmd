curl "https://tac10058.service-now.com/api/now/table/cmdb/<SYSID>?sysparm_fields=support_group%2Csys_tags%2Clocation&sysparm_input_display_value=%3CGROUP%3E%2C%3CTAG%3E%2C%3CLOCATION%3E" \
--request PATCH \
--header "Accept:application/json" \
--user 'admin':'admin'


