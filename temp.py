from repos import projects
import os

set1 = [
    {
        "repo": "io/repos/Activiti-b11f757a48600e53aaf3fcb7a3ba1ece6c463cb4/activiti-spring-boot-starter/src",
        "identifier": "Activiti-b11f757a48600e53aaf3fcb7a3ba1ece6c463cb4-activiti-spring-boot-starter"
    },
    {
        "repo": "io/repos/fastjson-5c6d6fd471ea1fab59f0df2dd31e0b936806780d/src",
        "identifier": "fastjson-5c6d6fd471ea1fab59f0df2dd31e0b936806780d-"
    },
    {
        "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-common-project/hadoop-auth/src",
        "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-common-project-hadoop-auth"
    },
    {
        "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-hdfs-project/hadoop-hdfs-nfs/src",
        "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-hdfs-project-hadoop-hdfs-nfs"
    },
    {
        "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-mapreduce-project/hadoop-mapreduce-client/hadoop-mapreduce-client-app/src",
        "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-mapreduce-project-hadoop-mapreduce-client-hadoop-mapreduce-client-app"
    },
    {
        "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-mapreduce-project/hadoop-mapreduce-client/hadoop-mapreduce-client-core/src",
        "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-mapreduce-project-hadoop-mapreduce-client-hadoop-mapreduce-client-core",
        "original_order": "order"
    },
    {
        "repo": "io/repos/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-mapreduce-project/hadoop-mapreduce-client/hadoop-mapreduce-client-hs/src",
        "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-hadoop-mapreduce-project-hadoop-mapreduce-client-hadoop-mapreduce-client-hs",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-cluster/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-cluster",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-common/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-common",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-config/dubbo-config-api/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-config-dubbo-config-api",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-filter/dubbo-filter-cache/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-filter-dubbo-filter-cache",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-rpc/dubbo-rpc-api/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-rpc-dubbo-rpc-api",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-rpc/dubbo-rpc-dubbo/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-rpc-dubbo-rpc-dubbo",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-serialization/dubbo-serialization-fst/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-dubbo-serialization-dubbo-serialization-fst",
        "original_order": "order"
    },
    {
        "repo": "io/repos/Struts-13d9053050c9e4fb2ef049db6a37d3f6eebf48fa/plugins/portlet/src",
        "identifier": "Struts-13d9053050c9e4fb2ef049db6a37d3f6eebf48fa-plugins-portlet",
        "original_order": "order"
    },
    {
        "repo": "io/repos/c2mon-d80687b119c713dd177a58cf53a997d8cc5ca264/c2mon-server/c2mon-server-elasticsearch/src",
        "identifier": "c2mon-d80687b119c713dd177a58cf53a997d8cc5ca264-c2mon-server-c2mon-server-elasticsearch",
        "original_order": "order"
    },
    {
        "repo": "io/repos/cukes-b483e1a8f261b80a66291a42fc455256b0b5059c/cukes-http/src",
        "identifier": "cukes-b483e1a8f261b80a66291a42fc455256b0b5059c-cukes-http",
        "original_order": "order"
    },
    {
        "repo": "io/repos/Achilles-e3099bdce342910951c4862c78751fd81ed4552e/integration-test-2_1/src",
        "identifier": "Achilles-e3099bdce342910951c4862c78751fd81ed4552e-integration-test-2_1",
        "original_order": "order"
    },



    {
        "repo": "io/repos/Achilles-e3099bdce342910951c4862c78751fd81ed4552e/integration-test-2_2/src",
        "identifier": "Achilles-e3099bdce342910951c4862c78751fd81ed4552e-integration-test-2_2",
        "original_order": "order"
    },
    {
        "repo": "io/repos/Achilles-e3099bdce342910951c4862c78751fd81ed4552e/integration-test-3_10/src",
        "identifier": "Achilles-e3099bdce342910951c4862c78751fd81ed4552e-integration-test-3_10",
        "original_order": "order"
    },
    {
        "repo": "io/repos/Achilles-e3099bdce342910951c4862c78751fd81ed4552e/integration-test-3_7/src",
        "identifier": "Achilles-e3099bdce342910951c4862c78751fd81ed4552e-integration-test-3_7",
        "original_order": "order"
    },
    {
        "repo": "io/repos/dropwizard-07dfaed697427e208d65049f80a5d1949833b7cd/dropwizard-logging/src",
        "identifier": "dropwizard-07dfaed697427e208d65049f80a5d1949833b7cd-dropwizard-logging",
        "original_order": "order"
    },
    {
        "repo": "io/repos/shardingsphere-elasticjob-b022898ef1b8c984e17efb2a422ee45f6b13e46e/elastic-job-lite-core/src",
        "identifier": "elastic-job-lite-b022898ef1b8c984e17efb2a422ee45f6b13e46e-elastic-job-lite-core",
        "original_order": "order"
    },
    {
        "repo": "io/repos/hsac-fitnesse-fixtures-a64c18d9c4bac8271275c7b089d40be20f0604b5/src",
        "identifier": "hsac-fitnesse-fixtures-a64c18d9c4bac8271275c7b089d40be20f0604b5-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-data-ebean-dd11b97654982403b50dd1d5369cadad71fce410/src",
        "identifier": "spring-data-ebean-dd11b97654982403b50dd1d5369cadad71fce410-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/jhipster-registry-00db36611da5fc7aaf9d5372aa90f2465d80c0c4/src",
        "identifier": "jhipster-registry-00db36611da5fc7aaf9d5372aa90f2465d80c0c4-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/http-request-2d62a3e9da726942a93cf16b6e91c0187e6c0136/lib/src",
        "identifier": "http-request-2d62a3e9da726942a93cf16b6e91c0187e6c0136-lib",
        "original_order": "order"
    },
    {
        "repo": "io/repos/marine-api-af0003847db9ba822f67d4f1dceb8de3fe63250a/src",
        "identifier": "marine-api-af0003847db9ba822f67d4f1dceb8de3fe63250a-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/openpojo-9badbcc4593e797accfed5e51bec9f2b843f0f67/src",
        "identifier": "openpojo-9badbcc4593e797accfed5e51bec9f2b843f0f67-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4/spring-boot-project/spring-boot-actuator-autoconfigure/src",
        "identifier": "spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4-spring-boot-project-spring-boot-actuator-autoconfigure",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4/spring-boot-project/spring-boot/src",
        "identifier": "spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4-spring-boot-project-spring-boot",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4/spring-boot-project/spring-boot-test-autoconfigure/src",
        "identifier": "spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4-spring-boot-project-spring-boot-test-autoconfigure",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4/spring-boot-project/spring-boot-test/src",
        "identifier": "spring-boot-daa3d457b71896a758995c264977bdd1414ee4d4-spring-boot-project-spring-boot-test",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-data-envers-5637994be37747e82b2d6d5b34555e2bee791fe6/src",
        "identifier": "spring-data-envers-5637994be37747e82b2d6d5b34555e2bee791fe6-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-ws-e8d89c9eb0929dda304174729c9c69fb29f448eb/spring-ws-core/src",
        "identifier": "spring-ws-e8d89c9eb0929dda304174729c9c69fb29f448eb-spring-ws-core",
        "original_order": "order"
    },
    {
        "repo": "io/repos/spring-ws-e8d89c9eb0929dda304174729c9c69fb29f448eb/spring-ws-security/src",
        "identifier": "spring-ws-e8d89c9eb0929dda304174729c9c69fb29f448eb-spring-ws-security",
        "original_order": "order"
    },
    {
        "repo": "io/repos/aismessages-7b0c4c708b6bb9a6da3d5737bcad1857ade8a931/src",
        "identifier": "aismessages-7b0c4c708b6bb9a6da3d5737bcad1857ade8a931-",
        "original_order": "order"
    },
    {
        "repo": "io/repos/unix4j-367da7d262e682a08577cdf19ebbbdd8a46870fe/unix4j-core/unix4j-command/src",
        "identifier": "unix4j-367da7d262e682a08577cdf19ebbbdd8a46870fe-unix4j-core-unix4j-command",
        "original_order": "order"
    },
    {
        "repo": "io/repos/admiral-e4b02936cc7d4ff2714e7231db0c4373ba5d48a2/compute/src",
        "identifier": "admiral-e4b02936cc7d4ff2714e7231db0c4373ba5d48a2-compute",
        "original_order": "order"
    },
    {
        "repo": "io/repos/admiral-e4b02936cc7d4ff2714e7231db0c4373ba5d48a2/request/src",
        "identifier": "admiral-e4b02936cc7d4ff2714e7231db0c4373ba5d48a2-request",
        "original_order": "order"
    },
    {
        "repo": "io/repos/Wikidata-Toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d/wdtk-dumpfiles/src",
        "identifier": "wikidata-toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d-wdtk-dumpfiles",
        "original_order": "order"
    },
    {
        "repo": "io/repos/Wikidata-Toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d/wdtk-util/src",
        "identifier": "wikidata-toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d-wdtk-util",
        "original_order": "order"
    },
    {
        "repo": "io/repos/wildfly-b19048b72669fc0e96665b1b125dc1fda21f5993/naming/src",
        "identifier": "wildfly-b19048b72669fc0e96665b1b125dc1fda21f5993-naming",
        "original_order": "order"
    },
    {
        "repo": "io/repos/wildfly-b19048b72669fc0e96665b1b125dc1fda21f5993/security/subsystem/src",
        "identifier": "wildfly-b19048b72669fc0e96665b1b125dc1fda21f5993-security-subsystem",
        "original_order": "order"
    },
    {
        "repo": "io/repos/wro4j-185ab607f1d649ca38b4a772831ee754cd4649fb/wro4j-core/src",
        "identifier": "wro4j-185ab607f1d649ca38b4a772831ee754cd4649fb-wro4j-core",
        "original_order": "order"
    },
    {
        "repo": "io/repos/carbon-apimgt-a82213e40e7e6aa529341fdd1d1c3de776949e64/components/apimgt/org.wso2.carbon.apimgt.core/src",
        "identifier": "carbon-apimgt-a82213e40e7e6aa529341fdd1d1c3de776949e64-components-apimgt-org.wso2.carbon.apimgt.core",
        "original_order": "order"
    },
    {
        "repo": "io/repos/riptide-8277e11fc069d8e24df0d233ef2577cc75659b75/riptide-spring-boot-starter/src",
        "identifier": "riptide-8277e11fc069d8e24df0d233ef2577cc75659b75-riptide-spring-boot-starter",
        "original_order": "order"
    }
]

set2 = [
    {
        "repo": "io/repos_two/easyexcel-756f16e42fbd7bc5c7fa18426cbc02fc81a42057/src",
        "identifier": "easyexcel-756f16e42fbd7bc5c7fa18426cbc02fc81a42057-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/fastjson-e05e9c5e4be580691cc55a59f3256595393203a1/src",
        "identifier": "fastjson-e05e9c5e4be580691cc55a59f3256595393203a1-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/Mapper-3c0b3307011fad53f811e08d05147d94fc6c0d67/base/src",
        "identifier": "Mapper-3c0b3307011fad53f811e08d05147d94fc6c0d67-se",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/nacos-525672272ecb00cd769a13c7b21a8e51cf873f25/api/src",
        "identifier": "nacos-525672272ecb00cd769a13c7b21a8e51cf873f25-i",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/Sentinel-7e2fa454fa0546c04142a268454faabac79370d0/sentinel-core/src",
        "identifier": "Sentinel-7e2fa454fa0546c04142a268454faabac79370d0-ntinel-core",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/alien4cloud-eb57d0feca6c37e0a4aafc3feef494e43e02ecda/alien4cloud-security/src",
        "identifier": "alien4cloud-eb57d0feca6c37e0a4aafc3feef494e43e02ecda-ien4cloud-security",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/archiva-292dbe1bb4323dd299d36b78f37d9c1d55c889f8/archiva-modules/archiva-base/archiva-repository-layer/src",
        "identifier": "archiva-292dbe1bb4323dd299d36b78f37d9c1d55c889f8-chiva-modules-archiva-base-archiva-repository-layer",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/cxf-69925893ed0e8a8fdfe1164b4e097a5cf5524027/core/src",
        "identifier": "cxf-69925893ed0e8a8fdfe1164b4e097a5cf5524027-re",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-serialization/dubbo-serialization-fst/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-bbo-serialization-dubbo-serialization-fst",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-1f84cdcfede5ec9843ecebf39a25d9b995b8098b/dubbo-common/src",
        "identifier": "dubbo-1f84cdcfede5ec9843ecebf39a25d9b995b8098b-bbo-common",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-5349c13a36d277a090e1dc68fbe7c3b46d78fc90/dubbo-common/src",
        "identifier": "dubbo-5349c13a36d277a090e1dc68fbe7c3b46d78fc90-bbo-common",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-registry/dubbo-registry-default/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-bbo-registry-dubbo-registry-default",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-cluster/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-bbo-cluster",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-rpc/dubbo-rpc-dubbo/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-bbo-rpc-dubbo-rpc-dubbo",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7/dubbo-rpc/dubbo-rpc-api/src",
        "identifier": "dubbo-737f7a7ea67832d7f17517326fb2491d0a086dd7-bbo-rpc-dubbo-rpc-api",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea/hadoop-hdfs-project/hadoop-hdfs-nfs/src",
        "identifier": "hadoop-cc2babc1f75c93bf89a8f10da525f944c15d02ea-doop-hdfs-project-hadoop-hdfs-nfs",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/hadoop-a585a73c3e02ac62350c136643a5e7f6095a3dbb/hadoop-hdfs-project/hadoop-hdfs-nfs/src",
        "identifier": "hadoop-a585a73c3e02ac62350c136643a5e7f6095a3dbb-doop-hdfs-project-hadoop-hdfs-nfs",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/ratis-bc9d7615d8ffa30e79a36b9fd1950af38f0f6a49/ratis-server/src",
        "identifier": "incubator-ratis-bc9d7615d8ffa30e79a36b9fd1950af38f0f6a49-tis-server",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/karaf-b368a87cba0f0e235d5dae72fd6c3559b50fb75c",
        "identifier": "karaf-b368a87cba0f0e235d5dae72fd6c3559b50fb75c-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/shardingsphere-elasticjob-b022898ef1b8c984e17efb2a422ee45f6b13e46e/elastic-job-lite-core/src",
        "identifier": "shardingsphere-elasticjob-b022898ef1b8c984e17efb2a422ee45f6b13e46e-astic-job-lite-core",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/shenyu-10375c5204c67f9889235f19fe2d6e8eb0438a5a/shenyu-client/shenyu-client-http/shenyu-client-springmvc/src",
        "identifier": "shenyu-10375c5204c67f9889235f19fe2d6e8eb0438a5a-enyu-client-shenyu-client-http-shenyu-client-springmvc",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/skywalking-edf0bce37f682c093d1ea5bcca0a6d2d1ecc2cc4/apm-commons/apm-datacarrier/src",
        "identifier": "skywalking-edf0bce37f682c093d1ea5bcca0a6d2d1ecc2cc4-m-commons-apm-datacarrier",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/struts-13d9053050c9e4fb2ef049db6a37d3f6eebf48fa/plugins/portlet/src",
        "identifier": "Struts-13d9053050c9e4fb2ef049db6a37d3f6eebf48fa-ugins-portlet",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/biojava-65ad15fe58dcedd258fee1c14505e424c8536efc/biojava-structure/src",
        "identifier": "biojava-65ad15fe58dcedd258fee1c14505e424c8536efc-ojava-structure",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/tessera-ecdd1a2ce6412c11a8ae722d7a4527a4a66da688/tessera-partyinfo/src",
        "identifier": "tessera-ecdd1a2ce6412c11a8ae722d7a4527a4a66da688-ssera-partyinfo",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/tessera-ecdd1a2ce6412c11a8ae722d7a4527a4a66da688/eclipselink-utils/src",
        "identifier": "tessera-ecdd1a2ce6412c11a8ae722d7a4527a4a66da688-lipselink-utils",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/cukes-b483e1a8f261b80a66291a42fc455256b0b5059c/cukes-http/src",
        "identifier": "cukes-b483e1a8f261b80a66291a42fc455256b0b5059c-kes-http",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/hutool-12969f248329f81f76eb5bece8c718ac1c63f7b1/hutool-core/src",
        "identifier": "hutool-12969f248329f81f76eb5bece8c718ac1c63f7b1-tool-core",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/hutool-12969f248329f81f76eb5bece8c718ac1c63f7b1/hutool-json/src",
        "identifier": "hutool-12969f248329f81f76eb5bece8c718ac1c63f7b1-tool-json",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/dropwizard-07dfaed697427e208d65049f80a5d1949833b7cd/dropwizard-logging/src",
        "identifier": "dropwizard-07dfaed697427e208d65049f80a5d1949833b7cd-opwizard-logging",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/jackson-databind-9b11650a6c3fee9ef9e3fb264d2244f65affc2ee/src",
        "identifier": "jackson-databind-9b11650a6c3fee9ef9e3fb264d2244f65affc2ee-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/jackson-dataformat-xml-2d08f8d0b0248a00c2c79b9a07e936b3287edb07/src",
        "identifier": "jackson-dataformat-xml-2d08f8d0b0248a00c2c79b9a07e936b3287edb07-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/hsac-fitnesse-fixtures-a64c18d9c4bac8271275c7b089d40be20f0604b5/src",
        "identifier": "hsac-fitnesse-fixtures-a64c18d9c4bac8271275c7b089d40be20f0604b5-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/spring-data-ebean-dd11b97654982403b50dd1d5369cadad71fce410/src",
        "identifier": "spring-data-ebean-dd11b97654982403b50dd1d5369cadad71fce410-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/jnr-posix-dbda72ce198a8dd766c30c591d63d726d2a28a7c/src",
        "identifier": "jnr-posix-dbda72ce198a8dd766c30c591d63d726d2a28a7c-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/marine-api-af0003847db9ba822f67d4f1dceb8de3fe63250a/src",
        "identifier": "marine-api-af0003847db9ba822f67d4f1dceb8de3fe63250a-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/java-e19a0ecbc9af258c43b486843df139c8ec8f117e/spring/src",
        "identifier": "java-e19a0ecbc9af258c43b486843df139c8ec8f117e-ring",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/light-4j-fcded1683dcbd41a968e221494778aa6b71e7428/consul/src",
        "identifier": "light-4j-fcded1683dcbd41a968e221494778aa6b71e7428-nsul",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/light-4j-fcded1683dcbd41a968e221494778aa6b71e7428/correlation/src",
        "identifier": "light-4j-fcded1683dcbd41a968e221494778aa6b71e7428-rrelation",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/light-4j-fcded1683dcbd41a968e221494778aa6b71e7428/handler/src",
        "identifier": "light-4j-fcded1683dcbd41a968e221494778aa6b71e7428-ndler",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/light-4j-fcded1683dcbd41a968e221494778aa6b71e7428/portal-registry/src",
        "identifier": "light-4j-fcded1683dcbd41a968e221494778aa6b71e7428-rtal-registry",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/light-4j-fcded1683dcbd41a968e221494778aa6b71e7428/metrics/src",
        "identifier": "light-4j-fcded1683dcbd41a968e221494778aa6b71e7428-trics",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/hippo4j-cf854b3cb3c47fd339421e5a46a3ae3229c53829/infra/common/src",
        "identifier": "hippo4j-cf854b3cb3c47fd339421e5a46a3ae3229c53829-fra-common",
        "original_order": "order",
    },
    # {
    #     "repo": "io/repos_two/Chronicle-Wire-27a9efc3ced000f46e0f46263614e08896058290/src",
    #     "identifier": "Chronicle-Wire-27a9efc3ced000f46e0f46263614e08896058290-",
    #     "original_order": "order",
    # },
    {
        "repo": "io/repos_two/openpojo-9badbcc4593e797accfed5e51bec9f2b843f0f67/src",
        "identifier": "openpojo-9badbcc4593e797accfed5e51bec9f2b843f0f67-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/junit-quickcheck-9361b6dae25b193782604d071754eb7fc566390a/guava/src",
        "identifier": "junit-quickcheck-9361b6dae25b193782604d071754eb7fc566390a-ava",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/junit-quickcheck-9361b6dae25b193782604d071754eb7fc566390a/core/src",
        "identifier": "junit-quickcheck-9361b6dae25b193782604d071754eb7fc566390a-re",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/secor-0927a127e3014ee494c97f8c0c25dafe9cf5ac27/src",
        "identifier": "secor-0927a127e3014ee494c97f8c0c25dafe9cf5ac27-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/querydsl-2bf234caf78549813a1e0f44d9c30ecc5ef734e3/querydsl-hibernate-search/src",
        "identifier": "querydsl-2bf234caf78549813a1e0f44d9c30ecc5ef734e3-erydsl-hibernate-search",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/rest-assured-bbede9fff77d4f1b751cdada0bdf8fe8d928919a/modules/spring-web-test-client/src",
        "identifier": "rest-assured-bbede9fff77d4f1b751cdada0bdf8fe8d928919a-ring-web-test-client",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/rrd4j-5e0c9c7e138167388721a0620b95526e89fd6059/src",
        "identifier": "rrd4j-5e0c9c7e138167388721a0620b95526e89fd6059-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/spring-data-envers-5637994be37747e82b2d6d5b34555e2bee791fe6/src",
        "identifier": "spring-data-envers-5637994be37747e82b2d6d5b34555e2bee791fe6-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/spring-ws-e8d89c9eb0929dda304174729c9c69fb29f448eb/spring-ws-security/src",
        "identifier": "spring-ws-e8d89c9eb0929dda304174729c9c69fb29f448eb-ring-ws-security",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/aismessages-7b0c4c708b6bb9a6da3d5737bcad1857ade8a931/src",
        "identifier": "aismessages-7b0c4c708b6bb9a6da3d5737bcad1857ade8a931-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/unix4j-367da7d262e682a08577cdf19ebbbdd8a46870fe/unix4j-core/unix4j-command/src",
        "identifier": "unix4j-367da7d262e682a08577cdf19ebbbdd8a46870fe-ix4j-core-unix4j-command",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/undertow-d0efffad5d2034bb07525cac9b299dac72c3045d/websockets-jsr/src",
        "identifier": "undertow-d0efffad5d2034bb07525cac9b299dac72c3045d-bsockets-jsr",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/flow-26aacd3cdf51c7e0a18ae21318d366ce7f91be8a/flow-data/src",
        "identifier": "flow-26aacd3cdf51c7e0a18ae21318d366ce7f91be8a-ow-data",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/Wikidata-Toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d/wdtk-dumpfiles/src",
        "identifier": "wikidata-toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d-tk-dumpfiles",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/Wikidata-Toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d/wdtk-util/src",
        "identifier": "wikidata-toolkit-20de6f7f12319f54eb962ff6e8357b3f5695d54d-tk-util",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/wildfly-b19048b72669fc0e96665b1b125dc1fda21f5993/naming/src",
        "identifier": "wildfly-b19048b72669fc0e96665b1b125dc1fda21f5993-ming",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/jboot-4bffb4dff4ce5190917491a1b68f79efbfe99650/src",
        "identifier": "jboot-4bffb4dff4ce5190917491a1b68f79efbfe99650-",
        "original_order": "order",
    },
    {
        "repo": "io/repos_two/riptide-8277e11fc069d8e24df0d233ef2577cc75659b75/riptide-spring-boot-starter/src",
        "identifier": "riptide-8277e11fc069d8e24df0d233ef2577cc75659b75-ptide-spring-boot-starter",
        "original_order": "order",
    },
]

for p in set1+set2:
    if not p in projects:
        print(p["identifier"])