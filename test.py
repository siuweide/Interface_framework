import os
import json
import requests

x= {"orderType":"OUTBOUND","gfsOrderId":"oneList","isMerge":"N","sellerUserId":"testuser_houlingzhong","buyerUserId":"lilazngirl2303","sellerOrderCode":"OrderCode","warehouseCode":"US0001","VATNo":"","deliveryWay":"OSF820823","status":"WFD","buyerFullname":"JONATHAN MCCORMACK","buyerEmail":"bells20052000@yahoo.com","buyerPhone":"01540 661381","buyerCountry":"UK","buyerState":"Bitterfeld-Wolfen","buyerCity":"kingussie","buyerPostCode":"PH21 1he","doorplateNumbers":"","buyerCompany":"","buyerAddreess1":"mccormacks garage","buyerAddreess2":"newtonmore road","gfsOrderList":[{"gfsOrderId":"oneList"}],"productList":[{"productCode":"auto_sku21","specifications":"","productName":"api自动化商品002","productNameEn":"auto_sku21","orderQuantity":"1","transactionId":"31","itemId":"2323","reSelect":"Y","platformItemId":"2323"}],"deliveryWayName":"VAS - Self pick up service","warehouseName":"USWC Warehouse","vasList":"[]","isSubmit":"Y"}
json_x = json.dumps(x)
print(type(json_x))

data={
'form':json_x,
 'ajax': 1
}