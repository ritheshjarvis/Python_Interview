desc = """Security scans (SiESTA) were performed on the MySite 360 site(Site -2203) components and the vulnerability is found while performing the Nessus Internal scans.
The same vulnerability is found on all the servers mentioned in the ‘Components’ field.

-*CVE’s*-
-CVE-2022-1292, CVE-2022-1343, CVE-2022-1434, CVE-2022-1473-

-{*}Vulnerability{*}: Ubuntu 18.04 LTS / 20.04 LTS / 21.10 / 22.04 LTS : OpenSSL vulnerabilities (USN-5402-1)-
-*For more details refer to:* [https://www.tenable.com/plugins/nessus/160502]-

-*CVSS v3*-
-Base Score: 9.8-
-Temporal Score: 9.1-

*CVE’s*
CVE-2022-1292, CVE-2022-129

{*}Vulnerability{*}: OpenSSL 1.1.1 < 1.1.1o Vulnerability
*For more details refer to:* [https://www.tenable.com/plugins/nessus/160477]

*CVSS v3*
Base Score: 9.8
Temporal Score: 8.999

-*CVE’s*-
-CVE-2028-1293, CVE-2022-1343, CVE-2022-1434, CVE-2022-1473-

-{*}Vulnerability{*}: Ubuntu 18.04 LTS / 20.04 LTS / 21.10 / 22.04 LTS : OpenSSL vulnerabilities (USN-5402-1)-
-*For more details refer to:* [https://www.tenable.com/plugins/nessus/160502]-

-*CVSS v3*-
-Base Score: 9.8-
-Temporal Score: 9.1-
Please find attached scan reports for the components. Refer to tab 'E_vulnerabilities' in the report attached. (include both excel and pdf reports)"""

desc1 = """Security scans (SiESTA) were performed on the MySite 360 site(Site -2203) components and the vulnerability is found while performing the Nessus Internal scans.
The same vulnerability is found on all the servers mentioned in the ‘Components’ field.

Please find attached scan reports for the components. Refer to tab 'E_vulnerabilities' in the report attached. (include both excel and pdf reports)
|[201084|https://www.tenable.com/plugins/index.php?view=single&id=201084]|OpenSSL 1.1.1 < 1.1.1za Vulnerability|CVE-2024-5535|*Base Score:* 9.1
*Temporal Score:* 7.9|"""

desc2 = """Security scans (SiESTA) were performed on the MySite 360 site(Site-2203) components and the vulnerability is found while performing the Nessus Internal scans. 
The same vulnerability is found on all the servers mentioned in the 'Components' field.

CVE’s
CVE-2025-0762

Vulnerability:
Microsoft Edge (Chromium) < 132.0.2957.140 (CVE-2025-0762)
For more details refer to: https://www.tenable.com/plugins/nessus/https://www.tenable.com/plugins/nessus/214822

CVSS v3
Base Score: 8.8
Temporal Score: https://www.tenable.com/plugins/nessus/214822

Please find attached scan reports for the components. Refer to tab 'E_vulnerabilities' in the report attached. (include both excel and pdf reports)"""

def get_cves_and_check_ids_from_description(description):
    cves = []
    check_ids = []
    for cve in description.replace("\n", " ").replace(u'\xa0', u' ').replace('|', ' ').split(' '):
        cve = cve.strip(',').strip(')').strip('(').strip('\r').strip('|')
        # print(cve)
        if cve.startswith("CVE-"):
            cves.append(cve)
            # print("--------------> cve", cve)
        if "tenable.com" in cve:
            check_id_list = []
            check_id_text = cve.split('/')[-1].strip(']').strip(']*')
            if 'index' not in check_id_text:
                check_id_list.append(check_id_text)
            elif 'index' in check_id_text:
                check_id_list.append(check_id_text.split('=')[-1].split(']')[0].strip(']'))
            check_ids.append(', '.join(set(check_id_list)) if check_id_list else '')
    return list(set(cves)), list(set(check_ids))


# cve, check_id = get_cves_and_check_ids_from_description(desc)
# print(cve)
# print(check_id)

def remove_striked_out_cve_section_at_jira_description123(_description: str):
    for i in range(_description.count('-*CVE’s*-')):
        _description = _description[:_description.index("-*CVE’s*-")] + _description[_description.index("-Temporal"):]
        print(_description)
        print("-------------------", i)
    return _description

def remove_striked_out_cve_section_at_jira_description(_description: str) -> str:
    start_token = "-*CVE’s*-"
    end_token = "-Temporal"

    while start_token in _description and end_token in _description:
        try:
            start_index = _description.index(start_token)
            end_index = _description.index(end_token, start_index) + len(end_token)
            _description = _description[:start_index] + _description[end_index:]
        except ValueError:
            break  # If end_token not found after start_token, break the loop

    return _description

description = remove_striked_out_cve_section_at_jira_description(desc2)
cve, check_id = get_cves_and_check_ids_from_description(description)
print(cve)
print(check_id)




# def remove_striked_out_cve_section_at_jira_description_recursion(_description: str):
#     if _description.count('-*CVE’s*-') == 0:
#         return _description
#     else:
#         while _description.count('-*CVE’s*-') > 0:
#             _description = _description[:_description.index("-*CVE’s*-")] + _description[desc.index("-Temporal"):]
#             print(_description)
#             remove_striked_out_cve_section_at_jira_description_recursion(_description)
#     return _description

# print(remove_striked_out_cve_section_at_jira_description_recursion(desc))
# print(remove_striked_out_cve_section_at_jira_description(desc))
# print(desc.index("-*CVE’s*-"))
# print(desc.index("-Temporal"))
# print(desc[:desc.index("-*CVE’s*-")] + desc[desc.index("-Temporal"):])