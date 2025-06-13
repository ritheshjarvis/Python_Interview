desc = """Security scans (SiESTA) were performed on the MySite 360 site(Site -2203) and the vulnerability is found while performing the Nessus Internal scans.
The same vulnerability is found on all the servers mentioned in the ‘Components’ field.

*CVE’s*
CVE-2023-21930, CVE-2023-21937, CVE-2023-21938, CVE-2023-21939, CVE-2023-21948, CVE-2023-21949, CVE-2023-21950, CVE-2023-21951, CVE-2023-21954, CVE-2023-21967, CVE-2023-21968

{*}Vulnerability{*}: Oracle Java SE Multiple Vulnerabilities (April 2023 CPU)
*For more details refer to:* [https://www.tenable.com/plugins/nessus/174511]

*CVSS v3*
Base Score: 7.8
Temporal Score: 6.8

 

-*CVE’s*-
-CVE-2023-21930, CVE-2023-21937, CVE-2023-21938, CVE-2023-21939, CVE-2023-21954, CVE-2023-21967, CVE-2023-21968-

-{*}Vulnerability{*}: OpenJDK 8 <= 8u362 / 11.0.0 <= 11.0.18 / 17.0.0 <= 17.0.6 / 20.0.0 <= 20.0.0 Multiple Vulnerabilities (2023-04-18-
-*For more details refer to:* [https://www.tenable.com/plugins/nessus/174697]-

-*CVSS v3*-
-Base Score: 7.4-
-Temporal Score: 6.4-

Please find attached scan reports for the components. Refer to tab 'E_vulnerabilities' in the report attached. (include both excel and pdf reports)"""

print(desc.count('-CVE'))

if '-CVE' in desc:
    print("sfsf")