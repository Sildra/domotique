```dot
digraph HomeAutomation {
  layout = neato;
  overlap = false;
  splines = true;

  node [shape=box, style=filled, fillcolor="#ddd", 
      fontcolor="#222", color="#777", penwidth=1.2,
      fontname="Segoe UI"];

  edge [fontname="Segoe UI", fontsize=9, fontcolor="#222",
      arrowsize=0.8, penwidth=1.6];

  s [label="Système"];
  ta [label="Tahoma"];
  i [label="Interrupteurs"];
  e [label="Éclairage"];
  v [label="Volets"];
  t [label="Thermostat"];
  fp [label="Fil Pilote"];

  i -> s [label="EnOcean", color="#3a3"];
  i -> e [label="EnOcean", color="#3a3"];
  s -> ta [dir=both, label="Wi-fi", color="#cc3", len=1.7]
  s -> e [dir=both, label="EnOcean", color="#3a3"];
  ta -> v [dir=both, label="IO", color="#a33", len=1.3];
  ta -> t [dir=both, label="RTS", color="#c73", len=1.7];
  t -> fp [label="Radio", color="#c73"];
  t -> v [style=invis]
  ta -> fp [style=invis]
}
```