from tv_store import TV

tv1 = TV('TV 1', 30, 3)
tv2 = TV('TV 2', 3, 2)

tv1.display()
tv2.display()

tv3 = TV('TV 3', 40, 6, True, 'Samsung')
tv3.set_channel(121)
tv3.set_volume(8)
tv3.display()

tv4 = TV('TV 4', 120, 1, False, 'TCL')
tv4.turn_on()
tv4.channel_up()
tv4.volume_down()
tv4.display()