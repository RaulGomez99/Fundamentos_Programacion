
Met_2_pul = 39.3701;
MET_2_pie = 3.2808399;
met_2_yar = 1.09361;
Met_2_MIL = 0.000621371192;
MET_2_LEG = 0.000207125;

def main():

    print("Este programa pasa una distancia en metros introducida por")
    print("teclado a distintas unidades de medida britanicas.\n\n")

    METROS = float(input("Dame distancia en metros a convertir: ") )
    
    Pulgadas = METROS * Met_2_pul
    Pies     = METROS * MET_2_pie
    Yardas   = METROS * met_2_yar;
    Millas   = METROS * Met_2_MIL;
    Leguas=metros*MET_2_LEG;
    
    print ( "\nLa distancia de" , metros , "metros es:\n" )
    print ( "  " ,Pulgadas ,"pulgadas" )
    print ( "  " ,Pies ,"pies" )
    print ( "  " ,Yardas ,"yardas" )
    print ( "  " ,Millas ,"millas" )
    print ( "  " ,Leguas ,"leguas" )

if __name__ == '__main__':
    main()
