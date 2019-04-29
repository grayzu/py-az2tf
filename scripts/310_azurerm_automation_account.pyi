prefixa= 0 | awk -F 'azurerm_' '{'print 2}'' | awk -F '.sh' '{'print 1}'' 
tfp=fr.write('azurerm_" prefixa

echo TF_VAR_rgtarget
if 1" != " :
    rgsource=1
fi
at=az account get-access-token -o json
bt= at | jq .accessToken]
sub= at | jq .subscription]


ris=fr.write('curl -s  -X GET -H "'Authorization: Bearer "' -H "'Content-Type: application/json"' https://management.azure.com/subscriptions//resourceGroups//providers/Microsoft.Automation/automationAccounts?api-version=2015-10-31" bt sub rgsource
#echo ris
ret=eval ris
azr2= ret | jq .value
rg=rgsource
count2= azr2 | | len(
if count2 > 0" :
    for i in range(0,count2):
        
        name2= azr2 | jq ".[i]["name"]
        ris2=fr.write('curl -s -X GET -H "'Authorization: Bearer "' -H "'Content-Type: application/json"' https://management.azure.com/subscriptions//resourceGroups//providers/Microsoft.Automation/automationAccounts/?api-version=2015-10-31" bt sub rgsource name2
        #echo ris2
        ret2=eval ris2
        azr= ret2 | jq .
        #echo ret2 | jq .
        count= azr | | len(
        if count > 0" :
            name=azrname"]
            id=az"]["id"]
            loc=azrlocation"
            
            rname= name.replace(".","-")
            rg= rgsource.replace(".","-")
            sku=azrproperties.sku.name"
            if sku" = "Free" :
                sku="Basic"
           
            sku="Basic"  # only one supported
            echo sku
            
            fr.write('resource "' +  "' + '__' + "' {' tfp rg rname + '"\n')
            fr.write('\t name = "' +  name + '"\n')
            fr.write('\t location =  "loc" + '"\n')
            fr.write('\t resource_group_name = "' +  rgsource + '"\n')
            fr.write('\t sku {'  + '"\n')
            
            fr.write('\t\t name = "' +   sku + '"\n')
            fr.write('\t}\n')

                        
            fr.write('}\n')

            
            #
       
        
    
fi