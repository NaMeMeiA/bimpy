import impy

def set_light_theme():
    """ light style from Pacome Danhiez (user itamago) https://github.com/ocornut/imgui/pull/511#issuecomment-175719267 """
    
    style = impy.get_style()
    style.set_color(impy.Colors.Text, impy.Vec4(0.00, 0.00, 0.00, 1.00))
    style.set_color(impy.Colors.TextDisabled, impy.Vec4(0.60, 0.60, 0.60, 1.00))
    style.set_color(impy.Colors.WindowBg, impy.Vec4(0.94, 0.94, 0.94, 1.00))
    style.set_color(impy.Colors.ChildWindowBg, impy.Vec4(0.00, 0.00, 0.00, 0.00))
    style.set_color(impy.Colors.Border, impy.Vec4(0.00, 0.00, 0.00, 0.39))
    style.set_color(impy.Colors.BorderShadow, impy.Vec4(1.00, 1.00, 1.00, 0.10))
    style.set_color(impy.Colors.FrameBg, impy.Vec4(1.00, 1.00, 1.00, 1.00))
    style.set_color(impy.Colors.FrameBgHovered, impy.Vec4(0.26, 0.59, 0.98, 0.40))
    style.set_color(impy.Colors.FrameBgActive, impy.Vec4(0.26, 0.59, 0.98, 0.67))
    style.set_color(impy.Colors.TitleBg, impy.Vec4(0.96, 0.96, 0.96, 1.00))
    style.set_color(impy.Colors.TitleBgCollapsed, impy.Vec4(1.00, 1.00, 1.00, 0.51))
    style.set_color(impy.Colors.TitleBgActive, impy.Vec4(0.82, 0.82, 0.82, 1.00))
    style.set_color(impy.Colors.MenuBarBg, impy.Vec4(0.86, 0.86, 0.86, 1.00))
    style.set_color(impy.Colors.ScrollbarBg, impy.Vec4(0.98, 0.98, 0.98, 0.53))
    style.set_color(impy.Colors.ScrollbarGrab, impy.Vec4(0.69, 0.69, 0.69, 0.80))
    style.set_color(impy.Colors.ScrollbarGrabHovered, impy.Vec4(0.49, 0.49, 0.49, 0.80))
    style.set_color(impy.Colors.ScrollbarGrabActive, impy.Vec4(0.49, 0.49, 0.49, 1.00))
    style.set_color(impy.Colors.ComboBg, impy.Vec4(0.86, 0.86, 0.86, 0.99))
    style.set_color(impy.Colors.CheckMark, impy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(impy.Colors.SliderGrab, impy.Vec4(0.26, 0.59, 0.98, 0.78))
    style.set_color(impy.Colors.SliderGrabActive, impy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(impy.Colors.Button, impy.Vec4(0.26, 0.59, 0.98, 0.40))
    style.set_color(impy.Colors.ButtonHovered, impy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(impy.Colors.ButtonActive, impy.Vec4(0.06, 0.53, 0.98, 1.00))
    style.set_color(impy.Colors.Header, impy.Vec4(0.26, 0.59, 0.98, 0.31))
    style.set_color(impy.Colors.HeaderHovered, impy.Vec4(0.26, 0.59, 0.98, 0.80))
    style.set_color(impy.Colors.HeaderActive, impy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(impy.Colors.Column, impy.Vec4(0.39, 0.39, 0.39, 1.00))
    style.set_color(impy.Colors.ColumnHovered, impy.Vec4(0.26, 0.59, 0.98, 0.78))
    style.set_color(impy.Colors.ColumnActive, impy.Vec4(0.26, 0.59, 0.98, 1.00))
    style.set_color(impy.Colors.ResizeGrip, impy.Vec4(0.50, 0.50, 0.50, 1.00))
    style.set_color(impy.Colors.ResizeGripHovered, impy.Vec4(0.26, 0.59, 0.98, 0.67))
    style.set_color(impy.Colors.ResizeGripActive, impy.Vec4(0.26, 0.59, 0.98, 0.95))
    style.set_color(impy.Colors.CloseButton, impy.Vec4(0.59, 0.59, 0.59, 0.50))
    style.set_color(impy.Colors.CloseButtonHovered, impy.Vec4(0.98, 0.39, 0.36, 1.00))
    style.set_color(impy.Colors.CloseButtonActive, impy.Vec4(0.98, 0.39, 0.36, 1.00))
    style.set_color(impy.Colors.PlotLines, impy.Vec4(0.39, 0.39, 0.39, 1.00))
    style.set_color(impy.Colors.PlotLinesHovered, impy.Vec4(1.00, 0.43, 0.35, 1.00))
    style.set_color(impy.Colors.PlotHistogram, impy.Vec4(0.90, 0.70, 0.00, 1.00))
    style.set_color(impy.Colors.PlotHistogramHovered, impy.Vec4(1.00, 0.60, 0.00, 1.00))
    style.set_color(impy.Colors.TextSelectedBg, impy.Vec4(0.26, 0.59, 0.98, 0.35))
    style.set_color(impy.Colors.PopupBg, impy.Vec4(1.00, 1.00, 1.00, 0.94))
    style.set_color(impy.Colors.ModalWindowDarkening, impy.Vec4(0.20, 0.20, 0.20, 0.35))
    impy.set_style(style)
