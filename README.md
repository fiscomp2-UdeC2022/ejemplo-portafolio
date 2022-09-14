# Portafolio actividades de laboratorio - Física Computacional II (510240 - 2022)

Incluya evidencias de las actividades de laboratorio de su
asignatura. Este producto será evaluado mediante la plataforma
[GitHub](https://github.com). Es su responsabilidad mantener este
repositorio actualizado.

- El documento principal es [portafolio.tex](portafolio.tex).
- Para cada laboratorio, usted creará un documento de latex que será alojado en la carpeta [tex/](tex/), con imágenes en la subcarpeta [tex/img/](tex/img/).
- Si usted crea software (pogramas de python), estas deben estar alojadas en la carpeta [src](src/).


<details>
	<summary> Instrucciones para instalar y configurar Git </summary>

## Cómo instalar Git
Primero, debes instalar Git en tu sistema operativo:
- [Linux](https://git-scm.com/download/linux)
- [Mac](https://git-scm.com/download/mac)
- [Windows](https://git-scm.com/download/win)

## Configurar usuario
Si ves este documento, significa que ya creaste un usuario y
contraseña en [GitHub](https://github.com).

Luego, debes configurar git para poder comunicar tu computador con
GitHub. Para ello, abre la consola de Git en tu computador (o la
terminal en mac/linux) y escribe:

```git
git config --global user.name "Nombre Apellido"
git config --global user.email "usuario@email.com"
```

Por favor, usa tu nombre real en la primera línea.

A continuación, debes crear una [llave SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent). En la misma consola de Git, escribe:

```git
ssh-keygen -t ed25519 -C "usuario@email.com"
```

Esto creará un archivo `id_ed25519.pub` en tu carpeta personal (`~/.ssh/` en linux/mac, `C:\Users\tu_usuario\.ssh` en windows). **Copia el contenido de ese archivo**.

Finalmente, abre la configuración de GitHub y busca "SSH and GPG keys" ([o pincha este link](https://github.com/settings/keys)). A la derecha, verás un botón verde "New SSH key". En `título` escribe un texto descriptivo de la llave (por ejemplo, "mi computador personal"). En `Key`, pega el contenido del archivo `id_ed25519.pub`. Puedes ver más [detalles aquí](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

</details>

<details>
<summary> Instrucciones para descargar/actualizar este repositorio </summary>

## Cómo descargar este repositorio

Primero, en el botón "Code" (arriba a la derecha), selecciona "SSH" y luego copia el link, como se muestra en esta imágen:

![clone repo](img/clone-repo.png)

Luego, en tu computador, crea una carpeta donde guardarás los materiales de tus tareas,
por ejemplo `fiscomp2`. Dentro de esta carpeta, escribe el siguiente comando, que creará una carpeta (probablemente de nombre `portafolio-autor`) dentro `fiscomp2` y donde se descargarán los contenidos de este repositorio.


```git
git clone URL   # reemplaza URL por el link que copiaste
```



## Cómo subir tus respuestas al repositorio

Una vez hayas descargado el repositorio, puedes editar, agregar o eliminar los archivos que quieras normalmente dentro de la carpeta `portafolio-autor`). 

Para preparar los cambios de tu repositorio, escribe esta secuencia de comandos en la consola de git:

```git
git add <archivo1> <archivo2> ...
git commit -m "Un mensaje corto que describa los cambios"
```

Repite esta acción cada vez que edites, elimines o agregues archivos a tu trabajo.

Finalmente, antes de cerrar tu computador, asegurate de subir tus archivos a github con:
```git
git push
```
</details>


<details>
	<summary> Integración con Overleaf </summary>

## Integración con overleaf
Note que puede sincronizar este repositorio con [overleaf](https://www.overleaf.com). Así, puede editar los documentos `.tex` en overleaf y subirlos
(casi) inmeditamente a github con un simple click.

Primero, debe permitir que overleaf se comunique con GitHub (depende del tipo de cuenta que usted posee. Si no puede seguir los siguientes pasos, tendrá que editar sus documentos manualmente sin overleaf):
- Inicie sesión en overleaf y diríjase a la [configuración de su
  cuenta](https://www.overleaf.com/user/settings) (Account -> Account
  Settings).
  
- Busque la sección "GitHub Integration" y apriete en el botón "Link
  to your GitHub account". 
  
- En la nueva ventana, inicie sesión en GituHub si es que no lo ha
  hecho. Si aparece una lista de organizaciones, apriete "Grant" en
  cada una de ellas. Luego, apriete en "Authorize overleaf".
  

Una vez haya finalizado el proceso anterior, puede sincronizar sus proyectos entre GitHub y overleaf:
- En overleaf, seleccione "New project" en el menú izquierdo.
- En el menú que aparecerá, seleccione "Import from GitHub".
- Debe aparecer una lista con todos los repositorios en el que usted
  es dueño. Busque el repositorio donde se encuentran los
  documentos latex que quiere sincronizar y apriete en "Import to Overleaf".
  
Los cambios no se sincronizarán automáticamente, debe hacerlo manualmente:
- Seleccione "Menu" en la esquina superior izquierda.
- Luego, busque la opción "GitHub".
  - Si han habido cambios en GitHub, debe importar los cambios a Overleaf: Apriete en "Pull GitHub changes into Overleaf"
  - Si quiere exportar los cambios desde Overleaf, apriete "Push Overleaf changes into GitHub"

</details>


# Instrucciones generales de entrega

- Al final de cada laboratorio, debe subir las evidencias de que usted realizó las actividades **a este repositorio de
  [GitHub](https://github.com)**.
  
  **Cualquier tarea enviada por otro medio (e.g. e-mail) no será
  revisada**. Es su responsabilidad asegurarse que sus respuestas sean
  visibles en la plataforma. 

- Al final de semestre, se revisará un único documento `portafolio.pdf` que será generado con el archivo [portafolio.tex](portafolio.tex) incluido en este repositorio. 
  
  - En la carpeta [tex/img](tex/img), suba todas las imágenes que vaya a usar para
  apoyar las evidencias de trabajo. Asegúrese de explicar estas figuras en el archivo que corresponda dentro de la carpeta [tex](tex/).
  
  - En la carpeta `src`, suba todos los programas (escritos en python) que son necesarios para
  responder a la tarea. Asegúrese de explicarlos en donde corresponde en los archivos de la carpeta [tex](tex/), si no, no serán revisados.
  
- Este documento es **individual**, aunque no hay perjuicio de que puedan trabajar con otros compañeros/as
  para apoyarse. Sin embargo, **si sus respuestas son idénticas
  o muy similares a las de otros grupos, el profesor es libre de
  calificar con la nota mínima**. El plagio es sancionado por el
  reglamento de la Universidad. 
  
  En caso de plagio entre estudiantes, el profesor considerará como autor original a aquel que haya subido primero sus archivos a la plataforma.

- **Cada** falta ortográfica, ecuación rayada y uso de símbolos no
  justificados (como `$\blacksquare$`, `$\square$`, `q.e.d.`,
  `$\Rightarrow$`, `$\forall$`, `$\exists$`, `$\bot$`, entre otros),
  serán penalizados según rúbricas que se entregarán oportunamente.
  
  En este repositorio, encuentra [comentarios
  comunes](comentarios_comunes_informes_fisica__v20210903.pdf) que
  suelo entregar al corregir informes de física.
  





--- 
Este es un documento escrito en el formato [Markdown de
GitHub](https://guides.github.com/features/mastering-markdown/).
