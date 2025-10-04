from reactpy import component, html

@component
def Composer(text, set_text, on_send, is_loading):
    def on_key_down(e):
        if e.get("isComposing"):
            return

        k = (e.get("key") or e.get("code") or "").lower()
        kc = e.get("keyCode") or e.get("which")

        is_enter = (
            k in ("enter", "numpadenter") or
            kc == 13
        )
        no_shift = not (e.get("shiftKey") or False)

        if is_enter and no_shift:
            try:
                e["preventDefault"]()
            except Exception:
                pass
            on_send()

    return html.div({"class_name": "composer"},
        html.input({
            "class_name": "input",
            "type": "text",
            "placeholder": "Escribe un mensaje…",
            "value": text,
            "on_change": lambda e: set_text(e["target"]["value"]),
            "on_key_down": on_key_down,
            "autocomplete": "off",
            "disabled": is_loading,
        }),
        html.div(
            {"style": {"display": "flex", "gap": "8px"}},
            html.button({
                "class_name": "button",
                "type": "button",
                "on_click": lambda e: on_send(),
                "disabled": is_loading or not text.strip(),
            }, "Enviar"),
        )
    )
