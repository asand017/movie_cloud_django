function createImage(){
	var i = document.createElement("IMG");
	i.setAttribute("src", "{% static \"wordCloud/images/output.png\" %}");
	i.setAttribute("width", "60%");
	i.setAttribute("height", "auto");
	i.setAttribute("alt", "Generated Word Cloud")
	document.body.appendChild(i)
}
