import numpy as np
import plotly.express as px


def figure_infos_nutritionnelles(
    data, variable_nutritionnelle = 'energy-kcal_100g',
    coicop = "01.1.7.3.2", valeur_produit = 8
    ):
    
    example_coicop = data.loc[data['variable'] == variable_nutritionnelle]
    example_coicop = example_coicop.loc[example_coicop['coicop']==coicop]
    example_coicop['color'] = np.where(example_coicop['quantile'] == valeur_produit, "red", "royalblue")

    fig = px.bar(
        example_coicop,
        x='quantile', y='value', color = "color", template = "simple_white",
        title=variable_nutritionnelle,
        labels={
            "quantile": "",
            "value": "Par portion de 100g"
        }
    )
    fig.update_layout(showlegend=False)
    fig.update_layout(hovermode="x")
    fig.update_traces(
        hovertemplate="<br>".join([
            "Dixième n° %{x}",
            f"{variable_nutritionnelle}: " + " au moins %{y} par portion de 100g"
        ])
    )
    return fig


def figure_infos_notes(
    data, variable_note = 'nutriscore_grade',
    coicop = "01.1.7.3.2", note_produit = "B",
    title = "Nutriscore"
):
    example_coicop = data.loc[data['variable'] == variable_note]
    example_coicop = example_coicop.loc[example_coicop['coicop']==coicop]
    example_coicop['color'] = np.where(example_coicop['note'] == note_produit, "Note du produit", "Autres produits")

    fig = px.bar(
        example_coicop,
        x='note', y='value', color = "color", template = "simple_white",
        title=title,
        color_discrete_map={"Note produit": "red", "Autres produits": "royalblue"},
        labels={
            "note": "Note",
            "value": ""
        }
    )
    fig.update_xaxes(
        categoryorder='array',
        categoryarray= ['A', 'B', 'C', 'D', 'E'])
    fig.update_layout(showlegend=False)
    fig.update_layout(hovermode="x")
    fig.update_traces(
        hovertemplate="<br>".join([
            "Note %{x}",
            f"{variable_note}: " +" %{y} produits"
        ])
    )

    return fig


def plot_product_info(
    data, variable,
    stats_notes):

    fig = figure_infos_notes(
        stats_notes,
        variable_note = variable,
        coicop = data['coicop'].iloc[0],
        note_produit = data[variable].iloc[0],
        title = variable.split("_")[0].capitalize()
    )

    return fig

