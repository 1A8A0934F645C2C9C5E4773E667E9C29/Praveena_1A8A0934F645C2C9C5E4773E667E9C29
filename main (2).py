def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product ==targetProduct:
      indices.append(index)
  return indices
Product=["shoes","boot","loafer","shoes","sandal","shoes"]
target="shoes"
target="apple"
result=linearSearchProduct(Product,target)
print(result)