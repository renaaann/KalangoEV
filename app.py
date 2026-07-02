import os
import sys
import customtkinter as ctk
from PIL import Image, ImageTk

# Merda pro meu .exe funcionar, n sei pq n vai
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("dark")

POSITIVE_COLOR = "#1c7c4d"
POSITIVE_TEXT = "#4ade80"
NEGATIVE_COLOR = "#7c1c2c"
NEGATIVE_TEXT = "#f87171"

class KalangoEV(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("KalangoEV")
        
        img = ImageTk.PhotoImage(file=resource_path("icons/kalango-tips.ico"))
        self.iconphoto(False, img)

        self.geometry("380x760")
        self.minsize(340, 400)
        self.configure(fg_color="#131318")
        
        self.market_count = 2
        self.opposite_entries = []

        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True)

        self.setup_header()
        self.setup_markets()
        self.setup_results()
        self.build_EV()

        self.reset_contraria()
        
        self.after(250, lambda: self.iconbitmap(resource_path("icons/kalango-tips.ico")))

    def setup_header(self):
        header = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20, 10))

        header_title = ctk.CTkLabel(header, text="KalangoEV", text_color="#f2f2f5", font=ctk.CTkFont("Inter", size=17, weight="bold"))
        header_title.pack(side="top")

        header_desc = ctk.CTkLabel(header, text="Calculadora de Valor Esperado (EV)", font=ctk.CTkFont("Inter", size=14, weight="bold"), text_color="#f2f2f5")
        header_desc.pack(side="top")

    def setup_markets(self):
        card = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
        card.pack(fill="x", padx=20, pady=(0, 10))

        markets_label = ctk.CTkLabel(card, text="Número de Mercados", font=ctk.CTkFont("Inter", size=12), text_color="#8b8b98")
        markets_label.pack(anchor="w", pady=(0, 6))

        self.markets_dropdown = ctk.CTkOptionMenu(
            card,
            values=["2 Mercados", "3 Mercados", "4 Mercados"],
            fg_color="#232330",
            button_color="#232330",
            button_hover_color="#2c2c3a",
            text_color="#f2f2f5",
            dropdown_fg_color="#131318",
            command=self.on_market_change,
        )
        self.markets_dropdown.set("2 Mercados")
        self.markets_dropdown.pack(fill="x", pady=(0, 15))

        odd_analisada_label = ctk.CTkLabel(card, text="Odd Analisada", font=ctk.CTkFont("Inter", size=12), text_color="#8b8b98")
        odd_analisada_label.pack(anchor="w", pady=(0, 6))

        self.odd_analisada_entry = ctk.CTkEntry(card, fg_color="#232330", border_width=0, text_color="#f2f2f5", height=38)
        self.odd_analisada_entry.pack(fill="x", pady=(0, 15))

        self.opposite_container = ctk.CTkFrame(card, fg_color="transparent")
        self.opposite_container.pack(fill="x")

        self.opposite_odd_label = ctk.CTkLabel(card, text="Odd Encontrada", font=ctk.CTkFont(size=12), text_color="#8b8b98")
        self.opposite_odd_label.pack(anchor="w", pady=(5, 6))

        self.found_odd_entry = ctk.CTkEntry(card, fg_color="#232330", border_width=0, text_color="#f2f2f5", height=38)
        self.found_odd_entry.pack(fill="x")

        self.opposite_odd_desc = ctk.CTkLabel(card, text="Insira a odd que você vai apostar.", font=ctk.CTkFont(size=10), text_color="#8b8b98")
        self.opposite_odd_desc.pack(anchor="w", pady=(4, 15))

        self.calcualte_button = ctk.CTkButton(card, height=38, text="Calcular", text_color="#f2f2f5", command=self.calculate)
        self.calcualte_button.pack(fill="x")

    def setup_results(self):
        card = ctk.CTkFrame(self.scroll_frame, fg_color="#1b1b22", corner_radius=10)
        card.pack(fill="x", padx=20, pady=(5, 10))

        self.payout_row = self.build_card(card, "%", "Payout", "--")
        self.fair_odd_row = self.build_card(card, "◈", "Odd Justa", "--")
        self.kelly_row = self.build_card(card, "▽", "Stake (Kelly)", "--", last=True)

    def build_card(self, parent, icon, label, value, last=False):
        row = ctk.CTkFrame(parent, fg_color="transparent")
        row.pack(fill="x", padx=15, pady=(12, 0) if not last else (12, 15))

        left = ctk.CTkFrame(row, fg_color="transparent")
        left.pack(side="left")

        ctk.CTkLabel(left, text=icon, font=ctk.CTkFont(size=13), text_color="#3d7cf2", width=20).pack(side="left")
        ctk.CTkLabel(left, text=label, font=ctk.CTkFont(size=13), text_color="#f2f2f5").pack(side="left", padx=(8, 0))

        value_label = ctk.CTkLabel(row, text=value, font=ctk.CTkFont(size=14, weight="bold"), text_color="#f2f2f5")
        value_label.pack(side="right")

        return value_label

    def build_EV(self):
        self.ev_box = ctk.CTkFrame(self.scroll_frame, fg_color=POSITIVE_COLOR, corner_radius=10)
        self.ev_box.pack(fill="x", padx=20, pady=(0, 20))

        self.ev_title = ctk.CTkLabel(self.ev_box, text="Aposta de Valor Positivo (EV+)", font=ctk.CTkFont("Inter", size=13, weight="bold"), text_color=POSITIVE_TEXT)
        self.ev_title.pack(anchor="w", padx=15, pady=(12, 0))

        self.ev_value = ctk.CTkLabel(self.ev_box, text="--%", font=ctk.CTkFont("Inter", size=24, weight="bold"), text_color=POSITIVE_TEXT)
        self.ev_value.pack(anchor="w", padx=15, pady=(0, 12))

    def on_market_change(self, value):
        self.market_count = int(value.split(" ")[0])
        self.reset_contraria()

    def reset_contraria(self):
        for widget in self.opposite_container.winfo_children():
            widget.destroy()
        self.opposite_entries = []

        for i in range(self.market_count - 1):
            label_text = f"Odd Contrária {i + 1}"
            ctk.CTkLabel(self.opposite_container, text=label_text, font=ctk.CTkFont(size=12), text_color="#8b8b98").pack(anchor="w", pady=(0, 6))

            entry = ctk.CTkEntry(self.opposite_container, fg_color="#232330", border_width=0, text_color="#f2f2f5", height=38)
            entry.pack(fill="x", pady=(0, 15))
            self.opposite_entries.append(entry)

    def calculate(self):
        try:
            analyzed_odd = float(self.odd_analisada_entry.get().replace(",", "."))
            found_odd = float(self.found_odd_entry.get().replace(",", "."))
            opposite_odds = [
                float(entry.get().replace(",", ".")) for entry in self.opposite_entries
            ]
        except ValueError:
            return

        all_odds = [analyzed_odd] + opposite_odds
        implied_probs = [1 / odd for odd in all_odds if odd > 0]
        if not implied_probs:
            return

        total_implied_prob = sum(implied_probs)
        payout = 1 / total_implied_prob
        fair_prob = implied_probs[0] / total_implied_prob
        fair_odd = 1 / fair_prob

        ev = found_odd * fair_prob - 1
        b = found_odd - 1
        kelly_fraction = ev / b if b > 0 else 0
        kelly_fraction = max(kelly_fraction, 0)

        self.payout_row.configure(text=f"{payout * 100:.2f}%")
        self.fair_odd_row.configure(text=f"{fair_odd:.3f}")
        self.kelly_row.configure(text=f"{kelly_fraction * 100:.2f}%")

        is_positive = ev > 0
        box_color = POSITIVE_COLOR if is_positive else NEGATIVE_COLOR
        text_color = POSITIVE_TEXT if is_positive else NEGATIVE_TEXT
        title_text = "Aposta de Valor Positivo (EV+)" if is_positive else "Aposta de Valor Negativo (EV-)"

        self.ev_box.configure(fg_color=box_color)
        self.ev_title.configure(text=title_text, text_color=text_color)
        self.ev_value.configure(text=f"{ev * 100:.2f}%", text_color=text_color)


if __name__ == "__main__":
    app = KalangoEV()
    app.mainloop()