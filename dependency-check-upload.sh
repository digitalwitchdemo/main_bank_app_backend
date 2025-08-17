var_version=`date +"Time"-"%H:%M:%S"`
data=$(date +"%Y-%m-%d")
export data1=$data
password='EVbxF730QRSjEnNoupAiCX'
username='admin'
eng='DependencyCheck'
pro='Main-bank-backend-Dependency-check-scan'
#var-test='DependencyCheck'
product_type='main_bank_app_backend'

  
  curl -X 'POST' \
  'http://3.82.212.213::8080/api/v2/import-scan/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -H 'X-CSRFTOKEN: jMLrqI2hbGLDIUZUoQ0mJ1hcxg8CM8v4A1QqM2z71cqr0lKoMnyjiDvwRkkLAtDf' \
  -F "product_type_name=${product_type}" \
  -F "scan_date=$data1" \
  -F 'active=true' \
  -F 'verified=true' \
  -F "engagement_end_date=$data1" \
  -F "engagement_name=${eng}" \
  -F 'deduplication_on_engagement=true' \
  -F 'minimum_severity=Info' \
  -F 'create_finding_groups_for_all_findings=true' \
  -F 'environment=Development' \
  -F 'group_by=finding_title' \
  -F "version=${var_version}" \
  -F 'test_title=DependencyCheck' \
  -F "product_name=${pro}" \
  -F 'file=@./target/dependency-check-report.xml;type=application/xml' \
  -F 'auto_create_context=true' \
  -F 'scan_type=Dependency Check Scan'   \
  -F 'close_old_findings=true' \
  -F 'close_old_findings_product_scope=true' \
  -F 'lead=1' \
  -F 'tags=DependencyCheck' \
  -F 'branch_tag=secops' \
  -F 'service=DependencyCheck' \
   --user "${username}:${password}"
