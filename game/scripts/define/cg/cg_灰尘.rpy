label cg_灰尘_1:
    image cg教令院地下走廊_snow1 = Fixed(SnowBlossom("images/particle/snow_cg_1_1_1.png", 30, xspeed=(-50, 50), yspeed=(-40, -80), start=0, fast=True))
    image cg教令院地下走廊_snow2 = Fixed(SnowBlossom("images/particle/snow_cg_1_1_2.png", 30, xspeed=(-50, 50), yspeed=(-40, -80), start=0, fast=True))

    show cg教令院地下走廊_snow1 onlayer cg zorder 100
    show cg教令院地下走廊_snow2 onlayer cg zorder 100
    return
