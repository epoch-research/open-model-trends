import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio


def save_plot(fig, folder, filename, extensions=['png', 'svg', 'pdf'], scale=2):
    for ext in extensions:
        fig.write_image(folder + filename + '.' + ext, scale=scale)
    fig.write_html(folder + filename + '.html')
