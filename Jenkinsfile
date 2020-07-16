@Library(value='kids-first/aws-infra-jenkins-shared-libraries', changelog=false) _
ecs_service_type_1_standard {
    projectName                = "ncpi-api-fhir-service"
    orgFullName                = "kids-first"
    account                    = "chopd3b"
    environments               = "dev,qa,prd"
    docker_image_type          = "debian"
    create_default_iam_role    = "1"
    entrypoint_command         = "/home/smile/smilecdr/bin/smilecdr run"
    quick_deploy               = "true"
    container_port             = "8000"
    health_check_path          = "/endpoint-health"
    external_config_repo       = "false"
    dependencies               = "ecr,postgres_rds"
    vcpu_container             = "2048"
    memory_container           = "4096"
    vcpu_task                  = "2048"
    memory_task                = "4096"
    internal_app               = "false"
    additional_container_ports = "9000,9100"
    dev_cidr                   = "0.0.0.0/0"
    qa_cidr                    = "0.0.0.0/0"
}
