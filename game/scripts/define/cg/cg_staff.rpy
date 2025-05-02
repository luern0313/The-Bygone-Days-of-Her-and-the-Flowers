# staff
label cg_staff_1:
    camera cg:
        perspective True
        gl_depth True
        offset (0, 0)
        align (0.5, 0.5)

    show black onlayer cg:
        zpos -400
        zzoom True
        offset (0, 0)
        align (0.5, 0.5)

    show logo onlayer cg:
        zpos -400
        zzoom True
        offset (0, 0)
        align (0.5, 0.5)

    pause 19.0
    hide logo onlayer cg
    pause 2.0

    return


label cg_staff_2:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    show staff1 onlayer cg:
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    return


label cg_staff_3:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    show staff2 onlayer cg:
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    return


label cg_staff_4:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    show staff3 onlayer cg:
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    return


label cg_staff_5:
    camera cg:
        perspective True
        gl_depth True
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    show staff4 onlayer cg:
        zpos 0
        offset (0, 0)
        align (0.5, 0.5)

    return


