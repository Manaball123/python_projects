import math

#took me like 3hrs to rearrange

#^retard comment here

#e1 * 0.5 * m1 * vi1 ^ 2 + e2 * 0.5 * m2 * vi2 ^ 2 = 0.5 * m1 * vr1 ^ 2 + 0.5 * m2 * vr2 ^ 2
# m1 * vi1 + m2 * vi2 = m1 * vr1 + m2 * vr2
#m1, m2, vi1, vi2, vr1, vr2
#OMFG I AM A RETARD



#LOOK AT HERE RETARD:


#	[[vr1=vi1,vr2=vi2],[vr1=(2*m2*vi2+(m1-m2)*vi1)/(m2+m1),vr2=((m2-m1)*vi2+2*m1*vi1)/(m2+m1)]]

#by maxima

#(not retard)

#i wanna have gaysex with maxima :heart_eyes:
#(not literally tho)



def calc(m1, m2, v1, v2):

    #resp1 = (m1 * v1 + m2 * v2) * m2 
    #resp2 = 2 * m2 * (m1 + m2)
    #resp3 = (4 * m1 * m2 * (m2 * v2 * (2 * m1 * v1 + m2 * v2) + m1 * m2 * (v1 ** 2 - v2 ** 2))) ** 0.5  

    IM = m1 * v1 + m2 * v2
    IE = m1 * (v1 ** 2) + m2 * (v2 ** 2)

    """
    resp1 = 2 * IM * m2
    resp3 = (4 * (IM ** 2) * m2 - 4 * ((m2 ** 2) + m1 * m2) * ((IM ** 2) - m1 * IE)) ** 0.5
    resp2 = 2 * m2 * (m1 + m2)
    """

    #resp1 = 2 * IM * m2
    #resp2 = 2 * (m2 ** 2 + m1 * m2)
    #resp3 = ((-2 * IM * m2) ** 2 - 4 * (m2 ** 2 + m1 * m2) * (IM ** 2 - m1 * IE)) ** 0.5
    vr1=(2*m2*v2+(m1-m2)*v1)/(m2+m1)
    print(vr1)
    #print((resp1 - resp3) / resp2)





calc(0.18,0.032,27,0)