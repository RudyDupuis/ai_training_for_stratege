# Entrainement d'un model d'IA par renforcement pour le jeu de plateau Stratège

lien du projet : https://stratege.rd-tech.fr/
lien du code de jeu : https://github.com/RudyDupuis/stratege

### Convertir un model en json:

```shell
tensorflowjs_converter --input_format=tf_saved_model --output_format=tfjs_graph_model saved_model/X_agent2 tfjs_model/X_agent2/
```