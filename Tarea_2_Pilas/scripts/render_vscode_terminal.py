import os
from PIL import Image, ImageDraw, ImageFont

def render_vscode_window(title_file, lines_data, output_path, width=1280, height=720):
    # Palette - VS Code Dark Modern (Windows 11)
    BG_TITLEBAR = (30, 30, 30)
    BG_TERMINAL = (24, 24, 24)
    BG_STATUSBAR = (0, 122, 204) # VS Code Blue
    BORDER_COLOR = (45, 45, 45)
    
    TEXT_MUTED = (150, 150, 150)
    TEXT_WHITE = (220, 220, 220)
    TEXT_BLUE = (86, 156, 214)
    TEXT_CYAN = (78, 201, 176)
    TEXT_GREEN = (181, 206, 168)
    TEXT_YELLOW = (220, 220, 170)
    TEXT_ORANGE = (206, 145, 120)
    TEXT_RED = (244, 71, 71)

    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Fonts
    windir = os.environ.get('WINDIR', 'C:\\Windows')
    font_dir = os.path.join(windir, 'Fonts')
    
    try:
        font_ui = ImageFont.truetype(os.path.join(font_dir, 'segoeui.ttf'), 15)
        font_ui_bold = ImageFont.truetype(os.path.join(font_dir, 'segoeuib.ttf'), 15)
        font_ui_sm = ImageFont.truetype(os.path.join(font_dir, 'segoeui.ttf'), 13)
        font_code = ImageFont.truetype(os.path.join(font_dir, 'consola.ttf'), 18)
        font_code_bold = ImageFont.truetype(os.path.join(font_dir, 'consolab.ttf'), 18)
    except:
        font_ui = ImageFont.load_default()
        font_ui_bold = font_ui
        font_ui_sm = font_ui
        font_code = font_ui
        font_code_bold = font_ui

    # 1. Main Background and Border (Rounded corners for Windows 11)
    radius = 12
    draw.rounded_rectangle([(0, 0), (width - 1, height - 1)], radius=radius, fill=BG_TERMINAL, outline=BORDER_COLOR, width=1)

    # 2. Windows 11 / VS Code Titlebar (Height 40px)
    titlebar_h = 42
    draw.rounded_rectangle([(0, 0), (width - 1, titlebar_h)], radius=radius, fill=BG_TITLEBAR)
    draw.rectangle([(0, titlebar_h - 6), (width - 1, titlebar_h)], fill=BG_TITLEBAR) # flatten bottom of titlebar
    draw.line([(0, titlebar_h), (width - 1, titlebar_h)], fill=BORDER_COLOR, width=1)

    # VS Code Icon placeholder (small blue chevron ribbon)
    icon_x, icon_y = 16, 12
    draw.polygon([(icon_x, icon_y+3), (icon_x+8, icon_y+9), (icon_x, icon_y+15)], fill=(0, 122, 204))
    draw.polygon([(icon_x+6, icon_y+3), (icon_x+14, icon_y+9), (icon_x+6, icon_y+15)], fill=(0, 122, 204))

    # Menu items
    menus = ["Archivo", "Editar", "Selección", "Ver", "Ir", "Ejecutar", "Terminal", "Ayuda"]
    mx = 44
    for m in menus:
        draw.text((mx, 12), m, font=font_ui_sm, fill=TEXT_MUTED)
        mx += int(draw.textlength(m, font=font_ui_sm)) + 14

    # Center Title: "ejercicioX.cpp - Tarea_2_Pilas - Visual Studio Code"
    full_title = f"{title_file} - Tarea_2_Pilas - Visual Studio Code"
    t_len = draw.textlength(full_title, font=font_ui)
    draw.text(((width - t_len) / 2, 11), full_title, font=font_ui, fill=TEXT_WHITE)

    # Windows 11 Native Controls on Top Right: Minimize, Maximize, Close
    # Minimize: '-'
    # Maximize: square
    # Close: 'X'
    cx = width - 138
    # Min
    draw.line([(cx + 15, 21), (cx + 27, 21)], fill=TEXT_MUTED, width=1)
    # Max
    draw.rectangle([(cx + 55, 15), (cx + 67, 27)], outline=TEXT_MUTED, width=1)
    # Close
    draw.line([(cx + 98, 15), (cx + 110, 27)], fill=TEXT_MUTED, width=1)
    draw.line([(cx + 98, 27), (cx + 110, 15)], fill=TEXT_MUTED, width=1)

    # 3. Terminal Panel Header (Height 36px)
    panel_y = titlebar_h + 1
    panel_h = 36
    draw.rectangle([(0, panel_y), (width - 1, panel_y + panel_h)], fill=(30, 30, 30))
    draw.line([(0, panel_y + panel_h), (width - 1, panel_y + panel_h)], fill=BORDER_COLOR, width=1)

    tabs = [
        ("PROBLEMAS", False),
        ("SALIDA", False),
        ("CONSOLA DE DEPURACIÓN", False),
        ("TERMINAL", True),
        ("PUERTOS", False)
    ]
    tx = 24
    for tab_name, active in tabs:
        tcolor = TEXT_WHITE if active else TEXT_MUTED
        draw.text((tx, panel_y + 9), tab_name, font=font_ui_bold if active else font_ui, fill=tcolor)
        t_w = int(draw.textlength(tab_name, font=font_ui_bold if active else font_ui))
        if active:
            # Underline for active tab
            draw.line([(tx, panel_y + panel_h - 2), (tx + t_w, panel_y + panel_h - 2)], fill=(0, 122, 204), width=2)
        tx += t_w + 22

    # Terminal dropdown & actions on right
    rx = width - 240
    # "1: pwsh" pill
    draw.rectangle([(rx, panel_y + 6), (rx + 110, panel_y + 30)], fill=(40, 40, 40), outline=(60, 60, 60))
    draw.text((rx + 12, panel_y + 9), "1: pwsh", font=font_ui_sm, fill=TEXT_WHITE)
    draw.polygon([(rx + 90, panel_y + 16), (rx + 96, panel_y + 16), (rx + 93, panel_y + 20)], fill=TEXT_MUTED)
    
    # Split, trash, chevron icons
    draw.text((rx + 125, panel_y + 9), "+", font=font_ui_bold, fill=TEXT_MUTED)
    draw.text((rx + 150, panel_y + 9), "^", font=font_ui_bold, fill=TEXT_MUTED)
    draw.text((rx + 175, panel_y + 9), "x", font=font_ui_bold, fill=TEXT_MUTED)

    # 4. Status Bar at Bottom (Height 26px)
    status_h = 26
    status_y = height - status_h
    draw.rounded_rectangle([(0, status_y), (width - 1, height - 1)], radius=radius, fill=BG_STATUSBAR)
    draw.rectangle([(0, status_y), (width - 1, status_y + 8)], fill=BG_STATUSBAR) # flatten top
    
    # Status bar left
    draw.text((16, status_y + 4), "main*   ⟳ 0", font=font_ui_sm, fill=(255, 255, 255))
    
    # Status bar right
    status_right = "Ln 1, Col 1   Espacios: 4   UTF-8   CRLF   C++   Windows (x64)"
    sr_w = draw.textlength(status_right, font=font_ui_sm)
    draw.text((width - sr_w - 20, status_y + 4), status_right, font=font_ui_sm, fill=(255, 255, 255))

    # 5. Terminal Body Content
    term_top = panel_y + panel_h + 16
    line_h = 24
    curr_y = term_top
    left_margin = 28

    for line in lines_data:
        # Check if special formatted line
        if isinstance(line, (list, tuple)):
            # Formatted parts [(text, color), (text, color), ...]
            curr_x = left_margin
            for text_part, col in line:
                draw.text((curr_x, curr_y), text_part, font=font_code, fill=col)
                curr_x += int(draw.textlength(text_part, font=font_code))
            curr_y += line_h
            continue
        else:
            # Single string auto-colored
            text = line
            color = TEXT_WHITE
            if text.startswith("PS C:"):
                # PowerShell Prompt
                # Split prompt and command
                parts = text.split("> ")
                if len(parts) == 2:
                    p1 = parts[0] + "> "
                    cmd = parts[1]
                    draw.text((left_margin, curr_y), p1, font=font_code, fill=TEXT_CYAN)
                    p1_w = int(draw.textlength(p1, font=font_code))
                    draw.text((left_margin + p1_w, curr_y), cmd, font=font_code, fill=TEXT_YELLOW)
                    curr_y += line_h
                    continue
            elif text.startswith("==") or text.startswith("--"):
                color = TEXT_BLUE
            elif text.startswith("Elemento") or text.startswith("Ingrese") or text.startswith("Seleccione"):
                color = TEXT_YELLOW
            elif "push" in text or "CORRECTO" in text or "VACIA" in text or "DESHACER" in text or "Tope:" in text:
                color = TEXT_GREEN
            elif "Error" in text or "INCORRECTO" in text:
                color = TEXT_RED
            elif text.startswith("  ->") or text.startswith("Extraccion"):
                color = (200, 220, 245)
            
            draw.text((left_margin, curr_y), text, font=font_code, fill=color)
        
        curr_y += line_h

    # Blinking cursor block
    cursor_x = left_margin
    # Check if last line had prompt
    # draw a prompt at the bottom
    prompt_str = "PS C:\\Users\\henry\\Desktop\\Tarea_2_Pilas\\codigo> "
    draw.text((left_margin, curr_y), prompt_str, font=font_code, fill=TEXT_CYAN)
    pw = int(draw.textlength(prompt_str, font=font_code))
    # Block cursor
    draw.rectangle([(left_margin + pw + 2, curr_y + 2), (left_margin + pw + 12, curr_y + 20)], fill=TEXT_WHITE)

    # Save
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Generado exitosamente: {output_path}")

print("Modulo cargado.")
