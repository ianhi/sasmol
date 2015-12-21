import os
import sasmol.sasmol as sasmol

def com_test(m):

    print 'com = ',m.calculate_center_of_mass()
    print 'com = ',m.calccom(0)

    m.setCom = m.calculate_center_of_mass()

    print 'm.com() = ',m.com()

    import sasmol.calculate as calculate

    print 'ugly = ',calculate.Calculate.calculate_center_of_mass(m)
    print 'uglier = ',calculate.Calculate.calccom(m,0)

    calc_com = calculate.Calculate.calculate_center_of_mass

    print 'prettier  = ',calc_com(m)


if __name__ == '__main__':

    pdbDataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','data','pdb_common')+os.path.sep

    m = sasmol.SasMol(0)

    try:
        m.read_pdb("hiv1_gag.pdb")
    except:
        m.read_pdb(pdbDataPath+"hiv1_gag.pdb")

    com_test(m)


