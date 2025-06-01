
# cve_list = ['CVE-2020-111111', 'CVE-2020-111112', 'CVE-2020-111113', 'CVE-2020-111114']
cve_list = ['CVE-2020-111114', 'CVE-2020-111113', 'CVE-2020-111114']
jira_description = ['CVE-2020-111113', 'CVE-2020-111114']

#
# for cve in cve_list:
#     print(cve)


print(list(set(cve_list)-set(jira_description)))

print(set(cve_list) == set(jira_description))
print(set(cve_list) == set(jira_description))
