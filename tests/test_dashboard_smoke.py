import unittest

import plotly.graph_objects as go

import dashboard


class DashboardSmokeTests(unittest.TestCase):
    """Smoke tests para validar se o dashboard principal está íntegro."""

    def test_layout_has_critical_components(self):
        ids = set()

        def walk(component):
            if hasattr(component, "id") and component.id is not None:
                ids.add(component.id)
            if hasattr(component, "children"):
                children = component.children
                if isinstance(children, list):
                    for child in children:
                        walk(child)
                elif children is not None:
                    walk(children)

        walk(dashboard.app.layout)

        for required_id in [
            "date-picker",
            "location-button",
            "location-dropdown",
            "line-graph",
            "choropleth-map",
            "bar-chart",
            "mortality-chart",
        ]:
            self.assertIn(required_id, ids)

    def test_callbacks_registered_for_critical_outputs(self):
        callback_outputs = set(dashboard.app.callback_map.keys())
        self.assertIn("line-graph.figure", callback_outputs)
        self.assertIn("choropleth-map.figure", callback_outputs)
        self.assertIn("bar-chart.figure", callback_outputs)
        self.assertIn("mortality-chart.figure", callback_outputs)

    def test_plot_line_graph_handles_invalid_metric(self):
        figure = dashboard.plot_line_graph("metrica-invalida", "BRASIL")
        self.assertIsInstance(figure, go.Figure)
        self.assertGreaterEqual(len(figure.data), 1)

    def test_update_map_returns_valid_figure(self):
        figure = dashboard.update_map(str(dashboard.max_date.date()))
        self.assertIsInstance(figure, go.Figure)

    def test_update_mortality_chart_handles_zero_division(self):
        figure = dashboard.update_mortality_chart(str(dashboard.max_date.date()))
        self.assertIsInstance(figure, go.Figure)
        self.assertGreaterEqual(len(figure.data), 1)


if __name__ == "__main__":
    unittest.main()
