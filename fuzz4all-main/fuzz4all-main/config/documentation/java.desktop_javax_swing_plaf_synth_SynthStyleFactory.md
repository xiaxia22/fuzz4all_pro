# Class SynthStyleFactory

**Source:** `java.desktop\javax\swing\plaf\synth\SynthStyleFactory.html`

### Class Description

```java
public abstract class
SynthStyleFactory

extends
Object
```

Factory used for obtaining

SynthStyle

s. Each of the
Synth

ComponentUI

s will call into the current

SynthStyleFactory

to obtain a

SynthStyle

for each of the distinct regions they have.

The following example creates a custom

SynthStyleFactory

that returns a different style based on the

Region

:

```java
class MyStyleFactory extends SynthStyleFactory {
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.BUTTON) {
return buttonStyle;
}
else if (id == Region.TREE) {
return treeStyle;
}
return defaultStyle;
}
}
SynthLookAndFeel laf = new SynthLookAndFeel();
UIManager.setLookAndFeel(laf);
SynthLookAndFeel.setStyleFactory(new MyStyleFactory());
```

**Since:** 1.5
**See Also:** SynthStyleFactory

,

SynthStyle

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthStyleFactory()

Creates a

SynthStyleFactory

.

---

### Method Details

#### public abstract
SynthStyle
getStyle​(
JComponent
c,

Region
id)

Returns the style for the specified Component.

**Parameters:**
- c

- Component asking for
- id

- Region identifier

**Returns:**
- SynthStyle for region.

---

### Additional Sections

#### Class SynthStyleFactory

java.lang.Object

- javax.swing.plaf.synth.SynthStyleFactory

javax.swing.plaf.synth.SynthStyleFactory

```java
public abstract class
SynthStyleFactory

extends
Object
```

Factory used for obtaining

SynthStyle

s. Each of the
Synth

ComponentUI

s will call into the current

SynthStyleFactory

to obtain a

SynthStyle

for each of the distinct regions they have.

The following example creates a custom

SynthStyleFactory

that returns a different style based on the

Region

:

```java
class MyStyleFactory extends SynthStyleFactory {
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.BUTTON) {
return buttonStyle;
}
else if (id == Region.TREE) {
return treeStyle;
}
return defaultStyle;
}
}
SynthLookAndFeel laf = new SynthLookAndFeel();
UIManager.setLookAndFeel(laf);
SynthLookAndFeel.setStyleFactory(new MyStyleFactory());
```

**Since:** 1.5
**See Also:** SynthStyleFactory

,

SynthStyle

public abstract class

SynthStyleFactory

extends

Object

Factory used for obtaining

SynthStyle

s. Each of the
Synth

ComponentUI

s will call into the current

SynthStyleFactory

to obtain a

SynthStyle

for each of the distinct regions they have.

The following example creates a custom

SynthStyleFactory

that returns a different style based on the

Region

:

```java
class MyStyleFactory extends SynthStyleFactory {
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.BUTTON) {
return buttonStyle;
}
else if (id == Region.TREE) {
return treeStyle;
}
return defaultStyle;
}
}
SynthLookAndFeel laf = new SynthLookAndFeel();
UIManager.setLookAndFeel(laf);
SynthLookAndFeel.setStyleFactory(new MyStyleFactory());
```

The following example creates a custom

SynthStyleFactory

that returns a different style based on the

Region

:

```java
class MyStyleFactory extends SynthStyleFactory {
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.BUTTON) {
return buttonStyle;
}
else if (id == Region.TREE) {
return treeStyle;
}
return defaultStyle;
}
}
SynthLookAndFeel laf = new SynthLookAndFeel();
UIManager.setLookAndFeel(laf);
SynthLookAndFeel.setStyleFactory(new MyStyleFactory());
```

class MyStyleFactory extends SynthStyleFactory {
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.BUTTON) {
return buttonStyle;
}
else if (id == Region.TREE) {
return treeStyle;
}
return defaultStyle;
}
}
SynthLookAndFeel laf = new SynthLookAndFeel();
UIManager.setLookAndFeel(laf);
SynthLookAndFeel.setStyleFactory(new MyStyleFactory());

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthStyleFactory

()

Creates a

SynthStyleFactory

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

SynthStyle

getStyle

​(

JComponent

c,

Region

id)

Returns the style for the specified Component.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SynthStyleFactory

()

Creates a

SynthStyleFactory

.

---

#### Constructor Summary

Creates a

SynthStyleFactory

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

SynthStyle

getStyle

​(

JComponent

c,

Region

id)

Returns the style for the specified Component.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the style for the specified Component.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthStyleFactory

```java
public SynthStyleFactory()
```

Creates a

SynthStyleFactory

.

============ METHOD DETAIL ==========

- Method Detail

- getStyle

```java
public abstract
SynthStyle
getStyle​(
JComponent
c,

Region
id)
```

Returns the style for the specified Component.

**Parameters:** c

- Component asking for
**Parameters:** id

- Region identifier
**Returns:** SynthStyle for region.

Constructor Detail

- SynthStyleFactory

```java
public SynthStyleFactory()
```

Creates a

SynthStyleFactory

.

---

#### Constructor Detail

SynthStyleFactory

```java
public SynthStyleFactory()
```

Creates a

SynthStyleFactory

.

---

#### SynthStyleFactory

public SynthStyleFactory()

Creates a

SynthStyleFactory

.

Method Detail

- getStyle

```java
public abstract
SynthStyle
getStyle​(
JComponent
c,

Region
id)
```

Returns the style for the specified Component.

**Parameters:** c

- Component asking for
**Parameters:** id

- Region identifier
**Returns:** SynthStyle for region.

---

#### Method Detail

getStyle

```java
public abstract
SynthStyle
getStyle​(
JComponent
c,

Region
id)
```

Returns the style for the specified Component.

**Parameters:** c

- Component asking for
**Parameters:** id

- Region identifier
**Returns:** SynthStyle for region.

---

#### getStyle

public abstract

SynthStyle

getStyle​(

JComponent

c,

Region

id)

Returns the style for the specified Component.

---

