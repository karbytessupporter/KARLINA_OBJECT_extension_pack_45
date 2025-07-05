# /**
#  * file: generate_vacuum_energy_flow.py
#  * type: python
#  * date: 05_JULY_2025
#  * author: karbytes
#  * license: PUBLIC_DOMAIN
#  */

import graphviz

dot = graphviz.Digraph(format='png')

dot.attr('node', shape='box', style='filled', color='lightgrey')
dot.node('A', 'Generative Vacuum')
dot.node('B', 'Spacetime Manifold\n(𝓜, g_{μν})')
dot.node('C', 'Vacuum Energy Density\nρ_vac = Λc² / 8πG')
dot.node('D', 'Metric Expansion\na(t) ~ e^{Ht}')
dot.node('E', 'Spatial Volume\nV(t)')
dot.node('F', 'Total Vacuum Energy\nE_vac = ρ_vac × V(t)')

dot.edge('A', 'B', label='Emergence of Spacetime')
dot.edge('B', 'C', label='Assign Λ')
dot.edge('C', 'D', label='Drives Expansion')
dot.edge('D', 'E', label='Compute Volume')
dot.edge('E', 'F', label='ρ_vac × V(t)')

dot.render('vacuum_energy_flow', cleanup=True)

print("Diagram saved as vacuum_energy_flow.png")
