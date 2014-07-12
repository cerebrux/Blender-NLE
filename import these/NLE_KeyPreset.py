import bpy
import os

wm = bpy.context.window_manager
kc = wm.keyconfigs.new(os.path.splitext(os.path.basename(__file__))[0])

# Map View2D
km = kc.keymaps.new('View2D', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('view2d.scroller_activate', 'LEFTMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroller_activate', 'MIDDLEMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.pan', 'MIDDLEMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.pan', 'MIDDLEMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('view2d.pan', 'TRACKPADPAN', 'ANY')
kmi = km.keymap_items.new('view2d.scroll_right', 'WHEELDOWNMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.scroll_left', 'WHEELUPMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.scroll_down', 'WHEELDOWNMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('view2d.scroll_up', 'WHEELUPMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('view2d.zoom_out', 'WHEELOUTMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom_in', 'WHEELINMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom_out', 'NUMPAD_MINUS', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom_in', 'NUMPAD_PLUS', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom', 'TRACKPADPAN', 'ANY', ctrl=True)
kmi = km.keymap_items.new('view2d.smoothview', 'TIMER1', 'ANY', any=True)
kmi = km.keymap_items.new('view2d.scroll_down', 'WHEELDOWNMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroll_up', 'WHEELUPMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroll_right', 'WHEELDOWNMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.scroll_left', 'WHEELUPMOUSE', 'PRESS')
kmi = km.keymap_items.new('view2d.zoom', 'MIDDLEMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('view2d.zoom', 'TRACKPADZOOM', 'ANY')
kmi = km.keymap_items.new('view2d.zoom_border', 'HOME', 'PRESS')

# Map Sequencer
km = kc.keymaps.new('Sequencer', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('sequencer.select_all', 'A', 'PRESS')
kmi.properties.action = 'TOGGLE'
kmi = km.keymap_items.new('sequencer.select_all', 'A', 'PRESS')
kmi.properties.action = 'INVERT'
kmi = km.keymap_items.new('sequencer.cut', 'B', 'PRESS')
kmi.properties.type = 'SOFT'
kmi = km.keymap_items.new('sequencer.cut', 'B', 'PRESS')
kmi.properties.type = 'HARD'
kmi = km.keymap_items.new('sequencer.mute', 'H', 'PRESS')
kmi.properties.unselected = False
kmi = km.keymap_items.new('sequencer.mute', 'H', 'PRESS', shift=True)
kmi.properties.unselected = True
kmi = km.keymap_items.new('sequencer.unmute', 'H', 'PRESS', alt=True)
kmi.properties.unselected = False
kmi = km.keymap_items.new('sequencer.unmute', 'H', 'PRESS', shift=True, alt=True)
kmi.properties.unselected = True
kmi = km.keymap_items.new('sequencer.lock', 'L', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.unlock', 'L', 'PRESS', shift=True, alt=True)
kmi = km.keymap_items.new('sequencer.reassign_inputs', 'R', 'PRESS')
kmi = km.keymap_items.new('sequencer.reload', 'R', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.reload', 'R', 'PRESS', shift=True, alt=True)
kmi.properties.adjust_length = True
kmi = km.keymap_items.new('sequencer.offset_clear', 'O', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.duplicate_move', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.delete', 'DEL', 'PRESS')
kmi = km.keymap_items.new('sequencer.delete', 'BACK_SPACE', 'PRESS')
kmi = km.keymap_items.new('sequencer.copy', 'C', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.paste', 'V', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.copy', 'C', 'PRESS', oskey=True)
kmi = km.keymap_items.new('sequencer.paste', 'V', 'PRESS', oskey=True)
kmi = km.keymap_items.new('sequencer.images_separate', 'Y', 'PRESS')
kmi = km.keymap_items.new('sequencer.meta_toggle', 'TAB', 'PRESS')
kmi = km.keymap_items.new('sequencer.meta_make', 'N', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.meta_separate', 'N', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.view_all', 'Z', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.view_selected', 'Z', 'PRESS')
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_UP', 'PRESS')
kmi.properties.next = True
kmi.properties.center = False
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_DOWN', 'PRESS')
kmi.properties.next = False
kmi.properties.center = False
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_UP', 'PRESS', alt=True)
kmi.properties.next = True
kmi.properties.center = True
kmi = km.keymap_items.new('sequencer.strip_jump', 'PAGE_DOWN', 'PRESS', alt=True)
kmi.properties.next = False
kmi.properties.center = True
kmi = km.keymap_items.new('sequencer.swap', 'LEFT_ARROW', 'PRESS', alt=True)
kmi.properties.side = 'LEFT'
kmi = km.keymap_items.new('sequencer.swap', 'RIGHT_ARROW', 'PRESS', alt=True)
kmi.properties.side = 'RIGHT'
kmi = km.keymap_items.new('sequencer.gap_remove', 'G', 'PRESS', ctrl=True)
kmi.properties.all = False
kmi = km.keymap_items.new('sequencer.gap_remove', 'G', 'PRESS', shift=True, ctrl=True)
kmi.properties.all = True
kmi = km.keymap_items.new('sequencer.gap_insert', 'G', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.snap', 'S', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.swap_inputs', 'S', 'PRESS', alt=True)
kmi = km.keymap_items.new('sequencer.cut_multicam', 'ONE', 'PRESS')
kmi.properties.camera = 1
kmi = km.keymap_items.new('sequencer.cut_multicam', 'TWO', 'PRESS')
kmi.properties.camera = 2
kmi = km.keymap_items.new('sequencer.cut_multicam', 'THREE', 'PRESS')
kmi.properties.camera = 3
kmi = km.keymap_items.new('sequencer.cut_multicam', 'FOUR', 'PRESS')
kmi.properties.camera = 4
kmi = km.keymap_items.new('sequencer.cut_multicam', 'FIVE', 'PRESS')
kmi.properties.camera = 5
kmi = km.keymap_items.new('sequencer.cut_multicam', 'SIX', 'PRESS')
kmi.properties.camera = 6
kmi = km.keymap_items.new('sequencer.cut_multicam', 'SEVEN', 'PRESS')
kmi.properties.camera = 7
kmi = km.keymap_items.new('sequencer.cut_multicam', 'EIGHT', 'PRESS')
kmi.properties.camera = 8
kmi = km.keymap_items.new('sequencer.cut_multicam', 'NINE', 'PRESS')
kmi.properties.camera = 9
kmi = km.keymap_items.new('sequencer.cut_multicam', 'ZERO', 'PRESS')
kmi.properties.camera = 10
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS')
kmi.properties.extend = False
kmi.properties.linked_handle = False
kmi.properties.left_right = False
kmi.properties.linked_time = False
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True)
kmi.properties.extend = True
kmi.properties.linked_handle = False
kmi.properties.left_right = False
kmi.properties.linked_time = False
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', alt=True)
kmi.properties.extend = False
kmi.properties.linked_handle = True
kmi.properties.left_right = False
kmi.properties.linked_time = False
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True, alt=True)
kmi.properties.extend = True
kmi.properties.linked_handle = True
kmi.properties.left_right = False
kmi.properties.linked_time = False
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi.properties.extend = False
kmi.properties.linked_handle = False
kmi.properties.left_right = True
kmi.properties.linked_time = True
kmi = km.keymap_items.new('sequencer.select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi.properties.extend = True
kmi.properties.linked_handle = False
kmi.properties.left_right = False
kmi.properties.linked_time = True
kmi = km.keymap_items.new('sequencer.select_more', 'NUMPAD_PLUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_less', 'NUMPAD_MINUS', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_linked_pick', 'L', 'PRESS')
kmi.properties.extend = False
kmi = km.keymap_items.new('sequencer.select_linked_pick', 'L', 'PRESS', shift=True)
kmi.properties.extend = True
kmi = km.keymap_items.new('sequencer.select_linked', 'L', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('sequencer.select_border', 'B', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.select_grouped', 'G', 'PRESS', shift=True)
kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', shift=True)
kmi.properties.name = 'SEQUENCER_MT_add'
kmi = km.keymap_items.new('wm.call_menu', 'C', 'PRESS')
kmi.properties.name = 'SEQUENCER_MT_change'
kmi = km.keymap_items.new('wm.context_set_int', 'O', 'PRESS')
kmi.properties.data_path = 'scene.sequence_editor.overlay_frame'
kmi.properties.value = 0
kmi = km.keymap_items.new('transform.seq_slide', 'G', 'PRESS')
kmi = km.keymap_items.new('transform.seq_slide', 'EVT_TWEAK_S', 'ANY')
kmi = km.keymap_items.new('transform.transform', 'E', 'PRESS')
kmi.properties.mode = 'TIME_EXTEND'
kmi = km.keymap_items.new('marker.add', 'M', 'PRESS')
kmi = km.keymap_items.new('marker.rename', 'M', 'PRESS', ctrl=True)

# Map SequencerPreview
km = kc.keymaps.new('SequencerPreview', space_type='SEQUENCE_EDITOR', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('sequencer.view_all_preview', 'Z', 'PRESS', shift=True)
kmi = km.keymap_items.new('sequencer.view_ghost_border', 'O', 'PRESS')
kmi = km.keymap_items.new('sequencer.view_zoom_ratio', 'NUMPAD_1', 'PRESS')
kmi.properties.ratio = 1.0
kmi = km.keymap_items.new('sequencer.sample', 'ACTIONMOUSE', 'PRESS')

# Map Markers
km = kc.keymaps.new('Markers', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('marker.add', 'M', 'PRESS')
kmi = km.keymap_items.new('marker.move', 'EVT_TWEAK_S', 'ANY')
kmi = km.keymap_items.new('marker.duplicate', 'D', 'PRESS', shift=True)
kmi = km.keymap_items.new('marker.select', 'SELECTMOUSE', 'PRESS')
kmi = km.keymap_items.new('marker.select', 'SELECTMOUSE', 'PRESS', shift=True)
kmi.properties.extend = True
kmi = km.keymap_items.new('marker.select', 'SELECTMOUSE', 'PRESS', ctrl=True)
kmi.properties.extend = False
kmi.properties.camera = True
kmi = km.keymap_items.new('marker.select', 'SELECTMOUSE', 'PRESS', shift=True, ctrl=True)
kmi.properties.extend = True
kmi.properties.camera = True
kmi = km.keymap_items.new('marker.select_border', 'B', 'PRESS')
kmi = km.keymap_items.new('marker.select_all', 'A', 'PRESS')
kmi = km.keymap_items.new('marker.delete', 'M', 'PRESS', shift=True)
kmi = km.keymap_items.new('marker.rename', 'M', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('marker.move', 'G', 'PRESS')
kmi = km.keymap_items.new('marker.camera_bind', 'B', 'PRESS', ctrl=True)

# Map Clip Editor
km = kc.keymaps.new('Clip Editor', space_type='CLIP_EDITOR', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('clip.view_pan', 'MIDDLEMOUSE', 'PRESS')
kmi = km.keymap_items.new('clip.view_pan', 'MIDDLEMOUSE', 'PRESS', shift=True)
kmi = km.keymap_items.new('clip.view_pan', 'TRACKPADPAN', 'ANY')
kmi = km.keymap_items.new('clip.view_zoom', 'MIDDLEMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('clip.view_zoom', 'TRACKPADZOOM', 'ANY')
kmi = km.keymap_items.new('clip.view_zoom', 'TRACKPADPAN', 'ANY', ctrl=True)
kmi = km.keymap_items.new('clip.view_zoom_in', 'WHEELINMOUSE', 'PRESS')
kmi = km.keymap_items.new('clip.view_zoom_out', 'WHEELOUTMOUSE', 'PRESS')
kmi = km.keymap_items.new('clip.view_zoom_in', 'NUMPAD_PLUS', 'PRESS')
kmi = km.keymap_items.new('clip.view_zoom_out', 'NUMPAD_MINUS', 'PRESS')
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_8', 'PRESS', ctrl=True)
kmi.properties.ratio = 8.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_4', 'PRESS', ctrl=True)
kmi.properties.ratio = 4.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_2', 'PRESS', ctrl=True)
kmi.properties.ratio = 2.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_8', 'PRESS', shift=True)
kmi.properties.ratio = 8.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_4', 'PRESS', shift=True)
kmi.properties.ratio = 4.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_2', 'PRESS', shift=True)
kmi.properties.ratio = 2.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_1', 'PRESS')
kmi.properties.ratio = 1.0
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_2', 'PRESS')
kmi.properties.ratio = 0.5
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_4', 'PRESS')
kmi.properties.ratio = 0.25
kmi = km.keymap_items.new('clip.view_zoom_ratio', 'NUMPAD_8', 'PRESS')
kmi.properties.ratio = 0.125
kmi = km.keymap_items.new('clip.view_all', 'HOME', 'PRESS')
kmi = km.keymap_items.new('clip.view_all', 'F', 'PRESS')
kmi.properties.fit_view = True
kmi = km.keymap_items.new('clip.view_selected', 'NUMPAD_PERIOD', 'PRESS')
kmi = km.keymap_items.new('clip.view_all', 'NDOF_BUTTON_FIT', 'PRESS')
kmi = km.keymap_items.new('clip.view_ndof', 'NDOF_MOTION', 'ANY')
kmi = km.keymap_items.new('clip.frame_jump', 'LEFT_ARROW', 'PRESS', shift=True, ctrl=True)
kmi.properties.position = 'PATHSTART'
kmi = km.keymap_items.new('clip.frame_jump', 'RIGHT_ARROW', 'PRESS', shift=True, ctrl=True)
kmi.properties.position = 'PATHEND'
kmi = km.keymap_items.new('clip.frame_jump', 'LEFT_ARROW', 'PRESS', shift=True, alt=True)
kmi.properties.position = 'FAILEDPREV'
kmi = km.keymap_items.new('clip.frame_jump', 'RIGHT_ARROW', 'PRESS', shift=True, alt=True)
kmi.properties.position = 'PATHSTART'
kmi = km.keymap_items.new('clip.change_frame', 'LEFTMOUSE', 'PRESS')
kmi = km.keymap_items.new('clip.select', 'SELECTMOUSE', 'PRESS')
kmi.properties.extend = False
kmi = km.keymap_items.new('clip.select', 'SELECTMOUSE', 'PRESS', shift=True)
kmi.properties.extend = True
kmi = km.keymap_items.new('clip.select_all', 'A', 'PRESS')
kmi.properties.action = 'TOGGLE'
kmi = km.keymap_items.new('clip.select_all', 'I', 'PRESS', ctrl=True)
kmi.properties.action = 'INVERT'
kmi = km.keymap_items.new('clip.select_border', 'B', 'PRESS')
kmi = km.keymap_items.new('clip.select_circle', 'C', 'PRESS')
kmi = km.keymap_items.new('wm.call_menu', 'G', 'PRESS', shift=True)
kmi.properties.name = 'CLIP_MT_select_grouped'
kmi = km.keymap_items.new('clip.select_lasso', 'EVT_TWEAK_A', 'ANY', ctrl=True, alt=True)
kmi.properties.deselect = False
kmi = km.keymap_items.new('clip.select_lasso', 'EVT_TWEAK_A', 'ANY', shift=True, ctrl=True, alt=True)
kmi.properties.deselect = True
kmi = km.keymap_items.new('clip.add_marker_slide', 'LEFTMOUSE', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('clip.delete_marker', 'DEL', 'PRESS', shift=True)
kmi = km.keymap_items.new('clip.delete_marker', 'M', 'PRESS', shift=True)
kmi = km.keymap_items.new('clip.slide_marker', 'LEFTMOUSE', 'PRESS')
kmi = km.keymap_items.new('clip.disable_markers', 'D', 'PRESS', shift=True)
kmi.properties.action = 'TOGGLE'
kmi = km.keymap_items.new('clip.delete_track', 'DEL', 'PRESS')
kmi = km.keymap_items.new('clip.delete_track', 'X', 'PRESS')
kmi = km.keymap_items.new('clip.lock_tracks', 'L', 'PRESS', ctrl=True)
kmi.properties.action = 'LOCK'
kmi = km.keymap_items.new('clip.lock_tracks', 'L', 'PRESS', alt=True)
kmi.properties.action = 'UNLOCK'
kmi = km.keymap_items.new('clip.hide_tracks', 'H', 'PRESS')
kmi.properties.unselected = False
kmi = km.keymap_items.new('clip.hide_tracks', 'H', 'PRESS', shift=True)
kmi.properties.unselected = True
kmi = km.keymap_items.new('clip.hide_tracks_clear', 'H', 'PRESS', alt=True)
kmi = km.keymap_items.new('clip.slide_plane_marker', 'LEFTMOUSE', 'PRESS')
kmi = km.keymap_items.new('clip.keyframe_insert', 'I', 'PRESS')
kmi = km.keymap_items.new('clip.keyframe_delete', 'I', 'PRESS', alt=True)
kmi = km.keymap_items.new('clip.join_tracks', 'J', 'PRESS', ctrl=True)
kmi = km.keymap_items.new('wm.call_menu', 'W', 'PRESS')
kmi.properties.name = 'CLIP_MT_tracking_specials'
kmi = km.keymap_items.new('wm.context_toggle', 'L', 'PRESS')
kmi.properties.data_path = 'space_data.lock_selection'
kmi = km.keymap_items.new('wm.context_toggle', 'D', 'PRESS', alt=True)
kmi.properties.data_path = 'space_data.show_disabled'
kmi = km.keymap_items.new('wm.context_toggle', 'S', 'PRESS', alt=True)
kmi.properties.data_path = 'space_data.show_marker_search'
kmi = km.keymap_items.new('wm.context_toggle', 'M', 'PRESS')
kmi.properties.data_path = 'space_data.use_mute_footage'
kmi = km.keymap_items.new('transform.translate', 'G', 'PRESS')
kmi = km.keymap_items.new('transform.translate', 'EVT_TWEAK_S', 'ANY')
kmi = km.keymap_items.new('transform.resize', 'S', 'PRESS')
kmi = km.keymap_items.new('transform.rotate', 'R', 'PRESS')
kmi = km.keymap_items.new('clip.clear_track_path', 'T', 'PRESS', alt=True)
kmi.properties.action = 'REMAINED'
kmi.properties.clear_active = False
kmi = km.keymap_items.new('clip.clear_track_path', 'T', 'PRESS', shift=True)
kmi.properties.action = 'UPTO'
kmi.properties.clear_active = False
kmi = km.keymap_items.new('clip.clear_track_path', 'T', 'PRESS', shift=True, alt=True)
kmi.properties.action = 'ALL'
kmi.properties.clear_active = False
kmi = km.keymap_items.new('clip.cursor_set', 'ACTIONMOUSE', 'PRESS')
kmi = km.keymap_items.new('wm.context_set_enum', 'COMMA', 'PRESS')
kmi.properties.data_path = 'space_data.pivot_point'
kmi.properties.value = 'BOUNDING_BOX_CENTER'
kmi = km.keymap_items.new('wm.context_set_enum', 'COMMA', 'PRESS', ctrl=True)
kmi.properties.data_path = 'space_data.pivot_point'
kmi.properties.value = 'MEDIAN_POINT'
kmi = km.keymap_items.new('wm.context_set_enum', 'PERIOD', 'PRESS')
kmi.properties.data_path = 'space_data.pivot_point'
kmi.properties.value = 'CURSOR'
kmi = km.keymap_items.new('wm.context_set_enum', 'PERIOD', 'PRESS', ctrl=True)
kmi.properties.data_path = 'space_data.pivot_point'
kmi.properties.value = 'INDIVIDUAL_ORIGINS'

# Map Frames
km = kc.keymaps.new('Frames', space_type='EMPTY', region_type='WINDOW', modal=False)

kmi = km.keymap_items.new('screen.frame_offset', 'UP_ARROW', 'PRESS', shift=True)
kmi.properties.delta = 10
kmi = km.keymap_items.new('screen.frame_offset', 'DOWN_ARROW', 'PRESS', shift=True)
kmi.properties.delta = -10
kmi = km.keymap_items.new('screen.frame_offset', 'LEFT_ARROW', 'PRESS')
kmi.properties.delta = -1
kmi = km.keymap_items.new('screen.frame_offset', 'RIGHT_ARROW', 'PRESS')
kmi.properties.delta = 1
kmi = km.keymap_items.new('screen.frame_offset', 'WHEELDOWNMOUSE', 'PRESS', alt=True)
kmi.properties.delta = 1
kmi = km.keymap_items.new('screen.frame_offset', 'WHEELUPMOUSE', 'PRESS', alt=True)
kmi.properties.delta = -1
kmi = km.keymap_items.new('screen.frame_jump', 'END', 'PRESS')
kmi.properties.end = True
kmi = km.keymap_items.new('screen.frame_jump', 'HOME', 'PRESS')
kmi.properties.end = False
kmi = km.keymap_items.new('screen.frame_jump', 'RIGHT_ARROW', 'PRESS', shift=True)
kmi.properties.end = True
kmi = km.keymap_items.new('screen.frame_jump', 'LEFT_ARROW', 'PRESS', shift=True)
kmi.properties.end = False
kmi = km.keymap_items.new('screen.keyframe_jump', 'UP_ARROW', 'PRESS')
kmi.properties.next = True
kmi = km.keymap_items.new('screen.keyframe_jump', 'DOWN_ARROW', 'PRESS')
kmi.properties.next = False
kmi = km.keymap_items.new('screen.keyframe_jump', 'MEDIA_LAST', 'PRESS')
kmi.properties.next = True
kmi = km.keymap_items.new('screen.keyframe_jump', 'MEDIA_FIRST', 'PRESS')
kmi.properties.next = False
kmi = km.keymap_items.new('screen.animation_play', 'L', 'PRESS')
kmi = km.keymap_items.new('screen.animation_play', 'J', 'PRESS')
kmi.properties.reverse = True
kmi = km.keymap_items.new('screen.animation_cancel', 'ESC', 'PRESS')
kmi = km.keymap_items.new('screen.animation_play', 'SPACE', 'PRESS')
kmi.properties.reverse = False
kmi = km.keymap_items.new('screen.animation_cancel', 'MEDIA_STOP', 'PRESS')

