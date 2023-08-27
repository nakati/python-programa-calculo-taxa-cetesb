print(" - cálculo de taxa para Cetesb em 2023 - ")
escolha=int(input("digite 1 para renovação ou 2 para licenciamento/ampliacao: "))
ufesp=float(34.26)
if escolha == 1:
    valorW=float(input("digite o valor do W:"))
    areaConstruida=float(input("digite o total das áreas (construidas/atividade ao ar livre: "))
    import math
    raizQuadrada=(math.sqrt(areaConstruida))
    cadaEtapa=100+(3*valorW*raizQuadrada)
    print(" ")
    print("valor em UFESP:      ", round(cadaEtapa, 2), "       >> valor em UFESP para ME/EPP:      ", round(cadaEtapa*0.15, 2))
    print("valor em REAIS: R$ ", round(cadaEtapa*ufesp, 2), "       >> valor em REAIS para ME/EPP: R$ ", round(cadaEtapa*ufesp*0.15, 2))
else:
    valorW = int(input("digite o valor do W:"))
    areaConstruida = float(input("digite o total das áreas (construídas/atividade ao ar livre/novos equipamentos: "))
    import math
    raizQuadrada = (math.sqrt(areaConstruida))
    cadaEtapa = 100 + (3 * valorW * raizQuadrada)
    print("segue valores:")
    print("LP/LI", "                                         LO")

    print("UFESP ", round(cadaEtapa, 2), " ou ",
          round(cadaEtapa * 0.15, 2), "(ME/EPP)", "           UFESP ", round(cadaEtapa, 2), " ou ",
          round(cadaEtapa * 0.15, 2), "(ME/EPP)")
    print("R$ ", round(cadaEtapa * ufesp, 2), " ou R$ ",
          round(cadaEtapa * ufesp * 0.15, 2),"(ME/EPP)", "        R$ ", round(cadaEtapa * ufesp, 2), " ou R$ ",
          round(cadaEtapa * ufesp * 0.15, 2),"(ME/EPP)")

    # SE HOUVER LP SEPARADO

    print("---------------------------------------------------------------------- ")
    print("SE HOUVER LP SEPARADO, INCLUIR:")
    print(" ")
    print("UFESP ", round(cadaEtapa, 2), " ou ",
         round(cadaEtapa * 0.15*0.3, 2), "(ME/EPP)")
    print("R$ ", round(cadaEtapa * ufesp*0.3, 2), " ou R$ ",
          round(cadaEtapa * ufesp * 0.15*0.3, 2), "(ME/EPP)")

