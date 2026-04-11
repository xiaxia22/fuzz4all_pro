# Class ColorUIResource

**Source:** `java.desktop\javax\swing\plaf\ColorUIResource.html`

### Class Description

```java
public class
ColorUIResource

extends
Color

implements
UIResource
```

A subclass of Color that implements UIResource. UI
classes that create colors should use this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Paint

,

Transparency

,

Serializable

,

UIResource

---

### Field Details

*No entries found.*

### Constructor Details

#### @ConstructorProperties
({"red","green","blue"})
public ColorUIResource​(int r,
int g,
int b)

Constructs a

ColorUIResource

.

**Parameters:**
- r

- the red component
- g

- the green component
- b

- the blue component

---

#### public ColorUIResource​(int rgb)

Constructs a

ColorUIResource

.

**Parameters:**
- rgb

- the combined RGB components

---

#### public ColorUIResource​(float r,
float g,
float b)

Constructs a

ColorUIResource

.

**Parameters:**
- r

- the red component
- g

- the green component
- b

- the blue component

---

#### public ColorUIResource​(
Color
c)

Constructs a

ColorUIResource

.

**Parameters:**
- c

- the color

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ColorUIResource

java.lang.Object

- java.awt.Color
- - javax.swing.plaf.ColorUIResource

java.awt.Color

- javax.swing.plaf.ColorUIResource

javax.swing.plaf.ColorUIResource

**All Implemented Interfaces:** Paint

,

Transparency

,

Serializable

,

UIResource

```java
public class
ColorUIResource

extends
Color

implements
UIResource
```

A subclass of Color that implements UIResource. UI
classes that create colors should use this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** UIResource

,

Serialized Form

public class

ColorUIResource

extends

Color

implements

UIResource

A subclass of Color that implements UIResource. UI
classes that create colors should use this class.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.awt.

Color

black

,

BLACK

,

blue

,

BLUE

,

cyan

,

CYAN

,

DARK_GRAY

,

darkGray

,

gray

,

GRAY

,

green

,

GREEN

,

LIGHT_GRAY

,

lightGray

,

magenta

,

MAGENTA

,

orange

,

ORANGE

,

pink

,

PINK

,

red

,

RED

,

white

,

WHITE

,

yellow

,

YELLOW

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ColorUIResource

​(float r,
float g,
float b)

Constructs a

ColorUIResource

.

ColorUIResource

​(int rgb)

Constructs a

ColorUIResource

.

ColorUIResource

​(int r,
int g,
int b)

Constructs a

ColorUIResource

.

ColorUIResource

​(

Color

c)

Constructs a

ColorUIResource

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.awt.

Color

brighter

,

createContext

,

darker

,

decode

,

equals

,

getAlpha

,

getBlue

,

getColor

,

getColor

,

getColor

,

getColorComponents

,

getColorComponents

,

getColorSpace

,

getComponents

,

getComponents

,

getGreen

,

getHSBColor

,

getRed

,

getRGB

,

getRGBColorComponents

,

getRGBComponents

,

getTransparency

,

hashCode

,

HSBtoRGB

,

RGBtoHSB

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.awt.

Color

black

,

BLACK

,

blue

,

BLUE

,

cyan

,

CYAN

,

DARK_GRAY

,

darkGray

,

gray

,

GRAY

,

green

,

GREEN

,

LIGHT_GRAY

,

lightGray

,

magenta

,

MAGENTA

,

orange

,

ORANGE

,

pink

,

PINK

,

red

,

RED

,

white

,

WHITE

,

yellow

,

YELLOW

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

Fields declared in class java.awt.

Color

black

,

BLACK

,

blue

,

BLUE

,

cyan

,

CYAN

,

DARK_GRAY

,

darkGray

,

gray

,

GRAY

,

green

,

GREEN

,

LIGHT_GRAY

,

lightGray

,

magenta

,

MAGENTA

,

orange

,

ORANGE

,

pink

,

PINK

,

red

,

RED

,

white

,

WHITE

,

yellow

,

YELLOW

---

#### Fields declared in class java.awt. Color

Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Fields declared in interface java.awt. Transparency

Constructor Summary

Constructors

Constructor

Description

ColorUIResource

​(float r,
float g,
float b)

Constructs a

ColorUIResource

.

ColorUIResource

​(int rgb)

Constructs a

ColorUIResource

.

ColorUIResource

​(int r,
int g,
int b)

Constructs a

ColorUIResource

.

ColorUIResource

​(

Color

c)

Constructs a

ColorUIResource

.

---

#### Constructor Summary

Constructs a

ColorUIResource

.

Method Summary

- Methods declared in class java.awt.

Color

brighter

,

createContext

,

darker

,

decode

,

equals

,

getAlpha

,

getBlue

,

getColor

,

getColor

,

getColor

,

getColorComponents

,

getColorComponents

,

getColorSpace

,

getComponents

,

getComponents

,

getGreen

,

getHSBColor

,

getRed

,

getRGB

,

getRGBColorComponents

,

getRGBComponents

,

getTransparency

,

hashCode

,

HSBtoRGB

,

RGBtoHSB

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.awt.

Color

brighter

,

createContext

,

darker

,

decode

,

equals

,

getAlpha

,

getBlue

,

getColor

,

getColor

,

getColor

,

getColorComponents

,

getColorComponents

,

getColorSpace

,

getComponents

,

getComponents

,

getGreen

,

getHSBColor

,

getRed

,

getRGB

,

getRGBColorComponents

,

getRGBComponents

,

getTransparency

,

hashCode

,

HSBtoRGB

,

RGBtoHSB

,

toString

---

#### Methods declared in class java.awt. Color

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- ColorUIResource

```java
@ConstructorProperties
({"red","green","blue"})
public ColorUIResource​(int r,
int g,
int b)
```

Constructs a

ColorUIResource

.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component

- ColorUIResource

```java
public ColorUIResource​(int rgb)
```

Constructs a

ColorUIResource

.

**Parameters:** rgb

- the combined RGB components

- ColorUIResource

```java
public ColorUIResource​(float r,
float g,
float b)
```

Constructs a

ColorUIResource

.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component

- ColorUIResource

```java
public ColorUIResource​(
Color
c)
```

Constructs a

ColorUIResource

.

**Parameters:** c

- the color

Constructor Detail

- ColorUIResource

```java
@ConstructorProperties
({"red","green","blue"})
public ColorUIResource​(int r,
int g,
int b)
```

Constructs a

ColorUIResource

.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component

- ColorUIResource

```java
public ColorUIResource​(int rgb)
```

Constructs a

ColorUIResource

.

**Parameters:** rgb

- the combined RGB components

- ColorUIResource

```java
public ColorUIResource​(float r,
float g,
float b)
```

Constructs a

ColorUIResource

.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component

- ColorUIResource

```java
public ColorUIResource​(
Color
c)
```

Constructs a

ColorUIResource

.

**Parameters:** c

- the color

---

#### Constructor Detail

ColorUIResource

```java
@ConstructorProperties
({"red","green","blue"})
public ColorUIResource​(int r,
int g,
int b)
```

Constructs a

ColorUIResource

.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component

---

#### ColorUIResource

@ConstructorProperties

({"red","green","blue"})
public ColorUIResource​(int r,
int g,
int b)

Constructs a

ColorUIResource

.

ColorUIResource

```java
public ColorUIResource​(int rgb)
```

Constructs a

ColorUIResource

.

**Parameters:** rgb

- the combined RGB components

---

#### ColorUIResource

public ColorUIResource​(int rgb)

Constructs a

ColorUIResource

.

ColorUIResource

```java
public ColorUIResource​(float r,
float g,
float b)
```

Constructs a

ColorUIResource

.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component

---

#### ColorUIResource

public ColorUIResource​(float r,
float g,
float b)

Constructs a

ColorUIResource

.

ColorUIResource

```java
public ColorUIResource​(
Color
c)
```

Constructs a

ColorUIResource

.

**Parameters:** c

- the color

---

#### ColorUIResource

public ColorUIResource​(

Color

c)

Constructs a

ColorUIResource

.

---

