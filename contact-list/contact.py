class contactEntity():
    def __init__(self, name, phone, email = ""):
        if not name and not phone and not email: return "name, phone and email is required, please fill in the required fields with string values"
        self.contact_extra_data = [
            {
                "image": "",
                "notes": ""
            }
        ]
        self.name = name
        self.phone = phone
        self.email = email
        self.isFavorite = False
      
    def add_extra_data(self, image_url: str = "", notes: str = ""):
        try:
            if not image_url and not notes: return "image_url or notes is required"

            self.contact_extra_data[0].update({"image": image_url, "notes": notes})
            return f"Informações adicionais do contato adicionadas com sucesso! \nImagem: {image_url} \nNotas: {notes}"
        except Exception as e:
            return str(e)
    
    def set_favorite(self, newFavorite: bool):
        try:
            self.isFavorite = newFavorite
            return print(f"Contato marcado como favorito: {newFavorite}")
        except Exception as e:
            return str(e)
    
    def edit_contact(self, name: str = "", phone: str = "", email: str = "") :
        try:
            fields = {"name": name, "phone": phone, "email": email}
            for key, value in fields.items():
                 if value:
                    setattr(self, key, value)

            return f"Contato editado com sucesso! \nNome: {self.name} \nTelefone: {self.phone} \nEmail: {self.email}"
        except Exception as e:
            return str(e)
        
    def __str__(self):
        return f"Informações do contato: \nNome: {self.name} \nTelefone: {self.phone} \nEmail: {self.email} \nFavorito: {self.isFavorite} \nNotas: {self.contact_extra_data[0].get('notes')} \nImagem: {self.contact_extra_data[0].get('image')}"
    
    def __repr__(self):
                return f"Informações do contato: \nNome: {self.name} \nTelefone: {self.phone} \nEmail: {self.email} \nFavorito: {self.isFavorite} \nNotas: {self.contact_extra_data[0].get('notes')} \nImagem: {self.contact_extra_data[0].get('image')}"