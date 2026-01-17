import pprint
Dicionário = {
    "identidade":{
        "nome" : "David Luís",
        "idade" : 19,
        "Cidade" : "Guaíba"
    },
    "identidade2":{
        "nome" : "fernando",
        "idade" : 12,
        "Cidade" : "Guaíba"
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(Dicionário)
print(Dicionário["identidade"]["nome"])