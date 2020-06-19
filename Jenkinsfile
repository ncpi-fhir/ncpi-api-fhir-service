@Library(value='kids-first/aws-infra-jenkins-shared-libraries', changelog=false) _
ecs_service_type_1_standard {
    projectName                = "ncpi-api-fhir-service"
    ecs_service_type_1_version = "feature/add-auth"
    deploy_scripts_version     = "feature/add-auth"
    orgFullName                = "kids-first"
    account                    = "chopd3b"
    environments               = "dev,qa"
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
    additional_container_ports = "9000,9100"
}
