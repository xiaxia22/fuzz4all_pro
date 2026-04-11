# Class BasicHTML

**Source:** `java.desktop\javax\swing\plaf\basic\BasicHTML.html`

### Class Description

```java
public class
BasicHTML

extends
Object
```

Support for providing html views for the swing components.
This translates a simple html string to a javax.swing.text.View
implementation that can render the html and provide the necessary
layout semantics.

**Since:** 1.3

---

### Field Details

#### public static final
String
propertyKey

Key to use for the html renderer when stored as a
client property of a JComponent.

**See Also:**
- Constant Field Values

---

#### public static final
String
documentBaseKey

Key stored as a client property to indicate the base that relative
references are resolved against. For example, lets say you keep
your images in the directory resources relative to the code path,
you would use the following the set the base:

```java
jComponent.putClientProperty(documentBaseKey,
xxx.class.getResource("resources/"));
```

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public BasicHTML()

*No description found.*

---

### Method Details

#### public static
View
createHTMLView​(
JComponent
c,

String
html)

Create an html renderer for the given component and
string of html.

**Parameters:**
- c

- a component
- html

- an HTML string

**Returns:**
- an HTML renderer

---

#### public static int getHTMLBaseline​(
View
view,
int w,
int h)

Returns the baseline for the html renderer.

**Parameters:**
- view

- the View to get the baseline for
- w

- the width to get the baseline for
- h

- the height to get the baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- FontMetrics

,

JComponent.getBaseline(int,int)

**Since:**
- 1.6

---

#### public static boolean isHTMLString​(
String
s)

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

**Parameters:**
- s

- a text

**Returns:**
- true

if the given string should trigger the
html rendering logic in a non-text component

---

#### public static void updateRenderer​(
JComponent
c,

String
text)

Stash the HTML render for the given text into the client
properties of the given JComponent. If the given text is

NOT HTML

the property will be cleared of any
renderer.

This method is useful for ComponentUI implementations
that are static (i.e. shared) and get their state
entirely from the JComponent.

**Parameters:**
- c

- a component
- text

- a text

---

### Additional Sections

#### Class BasicHTML

java.lang.Object

- javax.swing.plaf.basic.BasicHTML

javax.swing.plaf.basic.BasicHTML

```java
public class
BasicHTML

extends
Object
```

Support for providing html views for the swing components.
This translates a simple html string to a javax.swing.text.View
implementation that can render the html and provide the necessary
layout semantics.

**Since:** 1.3

public class

BasicHTML

extends

Object

Support for providing html views for the swing components.
This translates a simple html string to a javax.swing.text.View
implementation that can render the html and provide the necessary
layout semantics.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

documentBaseKey

Key stored as a client property to indicate the base that relative
references are resolved against.

static

String

propertyKey

Key to use for the html renderer when stored as a
client property of a JComponent.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicHTML

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

View

createHTMLView

​(

JComponent

c,

String

html)

Create an html renderer for the given component and
string of html.

static int

getHTMLBaseline

​(

View

view,
int w,
int h)

Returns the baseline for the html renderer.

static boolean

isHTMLString

​(

String

s)

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

static void

updateRenderer

​(

JComponent

c,

String

text)

Stash the HTML render for the given text into the client
properties of the given JComponent.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

documentBaseKey

Key stored as a client property to indicate the base that relative
references are resolved against.

static

String

propertyKey

Key to use for the html renderer when stored as a
client property of a JComponent.

---

#### Field Summary

Key stored as a client property to indicate the base that relative
references are resolved against.

Key to use for the html renderer when stored as a
client property of a JComponent.

Constructor Summary

Constructors

Constructor

Description

BasicHTML

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

View

createHTMLView

​(

JComponent

c,

String

html)

Create an html renderer for the given component and
string of html.

static int

getHTMLBaseline

​(

View

view,
int w,
int h)

Returns the baseline for the html renderer.

static boolean

isHTMLString

​(

String

s)

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

static void

updateRenderer

​(

JComponent

c,

String

text)

Stash the HTML render for the given text into the client
properties of the given JComponent.

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

Create an html renderer for the given component and
string of html.

Returns the baseline for the html renderer.

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

Stash the HTML render for the given text into the client
properties of the given JComponent.

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

============ FIELD DETAIL ===========

- Field Detail

- propertyKey

```java
public static final
String
propertyKey
```

Key to use for the html renderer when stored as a
client property of a JComponent.

**See Also:** Constant Field Values

- documentBaseKey

```java
public static final
String
documentBaseKey
```

Key stored as a client property to indicate the base that relative
references are resolved against. For example, lets say you keep
your images in the directory resources relative to the code path,
you would use the following the set the base:

```java
jComponent.putClientProperty(documentBaseKey,
xxx.class.getResource("resources/"));
```

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicHTML

```java
public BasicHTML()
```

============ METHOD DETAIL ==========

- Method Detail

- createHTMLView

```java
public static
View
createHTMLView​(
JComponent
c,

String
html)
```

Create an html renderer for the given component and
string of html.

**Parameters:** c

- a component
**Parameters:** html

- an HTML string
**Returns:** an HTML renderer

- getHTMLBaseline

```java
public static int getHTMLBaseline​(
View
view,
int w,
int h)
```

Returns the baseline for the html renderer.

**Parameters:** view

- the View to get the baseline for
**Parameters:** w

- the width to get the baseline for
**Parameters:** h

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** FontMetrics

,

JComponent.getBaseline(int,int)

- isHTMLString

```java
public static boolean isHTMLString​(
String
s)
```

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

**Parameters:** s

- a text
**Returns:** true

if the given string should trigger the
html rendering logic in a non-text component

- updateRenderer

```java
public static void updateRenderer​(
JComponent
c,

String
text)
```

Stash the HTML render for the given text into the client
properties of the given JComponent. If the given text is

NOT HTML

the property will be cleared of any
renderer.

This method is useful for ComponentUI implementations
that are static (i.e. shared) and get their state
entirely from the JComponent.

**Parameters:** c

- a component
**Parameters:** text

- a text

Field Detail

- propertyKey

```java
public static final
String
propertyKey
```

Key to use for the html renderer when stored as a
client property of a JComponent.

**See Also:** Constant Field Values

- documentBaseKey

```java
public static final
String
documentBaseKey
```

Key stored as a client property to indicate the base that relative
references are resolved against. For example, lets say you keep
your images in the directory resources relative to the code path,
you would use the following the set the base:

```java
jComponent.putClientProperty(documentBaseKey,
xxx.class.getResource("resources/"));
```

**See Also:** Constant Field Values

---

#### Field Detail

propertyKey

```java
public static final
String
propertyKey
```

Key to use for the html renderer when stored as a
client property of a JComponent.

**See Also:** Constant Field Values

---

#### propertyKey

public static final

String

propertyKey

Key to use for the html renderer when stored as a
client property of a JComponent.

documentBaseKey

```java
public static final
String
documentBaseKey
```

Key stored as a client property to indicate the base that relative
references are resolved against. For example, lets say you keep
your images in the directory resources relative to the code path,
you would use the following the set the base:

```java
jComponent.putClientProperty(documentBaseKey,
xxx.class.getResource("resources/"));
```

**See Also:** Constant Field Values

---

#### documentBaseKey

public static final

String

documentBaseKey

Key stored as a client property to indicate the base that relative
references are resolved against. For example, lets say you keep
your images in the directory resources relative to the code path,
you would use the following the set the base:

```java
jComponent.putClientProperty(documentBaseKey,
xxx.class.getResource("resources/"));
```

jComponent.putClientProperty(documentBaseKey,
xxx.class.getResource("resources/"));

Constructor Detail

- BasicHTML

```java
public BasicHTML()
```

---

#### Constructor Detail

BasicHTML

```java
public BasicHTML()
```

---

#### BasicHTML

public BasicHTML()

Method Detail

- createHTMLView

```java
public static
View
createHTMLView​(
JComponent
c,

String
html)
```

Create an html renderer for the given component and
string of html.

**Parameters:** c

- a component
**Parameters:** html

- an HTML string
**Returns:** an HTML renderer

- getHTMLBaseline

```java
public static int getHTMLBaseline​(
View
view,
int w,
int h)
```

Returns the baseline for the html renderer.

**Parameters:** view

- the View to get the baseline for
**Parameters:** w

- the width to get the baseline for
**Parameters:** h

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** FontMetrics

,

JComponent.getBaseline(int,int)

- isHTMLString

```java
public static boolean isHTMLString​(
String
s)
```

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

**Parameters:** s

- a text
**Returns:** true

if the given string should trigger the
html rendering logic in a non-text component

- updateRenderer

```java
public static void updateRenderer​(
JComponent
c,

String
text)
```

Stash the HTML render for the given text into the client
properties of the given JComponent. If the given text is

NOT HTML

the property will be cleared of any
renderer.

This method is useful for ComponentUI implementations
that are static (i.e. shared) and get their state
entirely from the JComponent.

**Parameters:** c

- a component
**Parameters:** text

- a text

---

#### Method Detail

createHTMLView

```java
public static
View
createHTMLView​(
JComponent
c,

String
html)
```

Create an html renderer for the given component and
string of html.

**Parameters:** c

- a component
**Parameters:** html

- an HTML string
**Returns:** an HTML renderer

---

#### createHTMLView

public static

View

createHTMLView​(

JComponent

c,

String

html)

Create an html renderer for the given component and
string of html.

getHTMLBaseline

```java
public static int getHTMLBaseline​(
View
view,
int w,
int h)
```

Returns the baseline for the html renderer.

**Parameters:** view

- the View to get the baseline for
**Parameters:** w

- the width to get the baseline for
**Parameters:** h

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** FontMetrics

,

JComponent.getBaseline(int,int)

---

#### getHTMLBaseline

public static int getHTMLBaseline​(

View

view,
int w,
int h)

Returns the baseline for the html renderer.

isHTMLString

```java
public static boolean isHTMLString​(
String
s)
```

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

**Parameters:** s

- a text
**Returns:** true

if the given string should trigger the
html rendering logic in a non-text component

---

#### isHTMLString

public static boolean isHTMLString​(

String

s)

Check the given string to see if it should trigger the
html rendering logic in a non-text component that supports
html rendering.

updateRenderer

```java
public static void updateRenderer​(
JComponent
c,

String
text)
```

Stash the HTML render for the given text into the client
properties of the given JComponent. If the given text is

NOT HTML

the property will be cleared of any
renderer.

This method is useful for ComponentUI implementations
that are static (i.e. shared) and get their state
entirely from the JComponent.

**Parameters:** c

- a component
**Parameters:** text

- a text

---

#### updateRenderer

public static void updateRenderer​(

JComponent

c,

String

text)

Stash the HTML render for the given text into the client
properties of the given JComponent. If the given text is

NOT HTML

the property will be cleared of any
renderer.

This method is useful for ComponentUI implementations
that are static (i.e. shared) and get their state
entirely from the JComponent.

This method is useful for ComponentUI implementations
that are static (i.e. shared) and get their state
entirely from the JComponent.

---

