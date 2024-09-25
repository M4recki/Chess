from pygame import image, transform

class Figure:
    """_summary_

    Raises:
        NotImplementedError: _description_
    """

    def __init__(self, color):
        self.color = color
        self.image = None

    def load_image(self, image_path):
        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (75, 75))

    def draw(self, x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_

        Raises:
            NotImplementedError: _description_
        """        
        raise NotImplementedError("Draw method must be implemented by subclass")


class Pawn(Figure):
    """_summary_"""

    def __init__(self, color):
        super().__init__(color)

    def draw(self, x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        self.screen.blit(self.image, (x * 75, y * 75))


class Rook(Figure):
    """_summary_

    Args:
        Figure (_type_): _description_
    """

    def __init__(self, color):
        super().__init__(color)

    def draw(self, x, y):
        self.screen.blit(self.image, (x * 75, y * 75))


class Bishop(Figure):
    """_summary_

    Args:
        Figure (_type_): _description_
    """

    def __init__(self, color):
        super().__init__(color)

    def draw(self, x, y):
        self.screen.blit(self.image, (x * 75, y * 75))


class Knight(Figure):
    """_summary_

    Args:
        Figure (_type_): _description_
    """

    def __init__(self, color):
        super().__init__(color)

    def draw(self, x, y):
        self.screen.blit(self.image, (x * 75, y * 75))


class Queen(Figure):
    """_summary_

    Args:
        Figure (_type_): _description_
    """

    def __init__(self, color):
        super().__init__(color)

    def draw(self, x, y):
        self.screen.blit(self.image, (x * 75, y * 75))


class King(Figure):
    """_summary_

    Args:
        Figure (_type_): _description_
    """

    def __init__(self, color):
        super().__init__(color)

    def draw(self, x, y):
        """_summary_

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        self.screen.blit(self.image, (x * 75, y * 75))
