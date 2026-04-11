# Annotation Type SwingContainer

**Source:** `java.desktop\javax\swing\SwingContainer.html`

### Class Description

```java
@Target
(
TYPE
)

@Retention
(
RUNTIME
)
public @interface
SwingContainer
```

An annotation used to specify some swing-related information
for the automatically generated

BeanInfo

classes.
This annotation is not used if the annotated class
has a corresponding user-defined

BeanInfo

class,
which does not imply the automatic analysis.

The

isContainer

feature attribute

was introduced primarily for the Swing library.
All Swing components extend the

Container

class by design, so the builder tool assumes that all Swing components
are containers. The

BeanInfo

classes
with the

isContainer

attribute allow to directly specify
whether a Swing component is a container or not.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### delegate

String The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

---

#### value

boolean The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

---

### Additional Sections

#### Annotation Type SwingContainer

```java
@Target
(
TYPE
)

@Retention
(
RUNTIME
)
public @interface
SwingContainer
```

An annotation used to specify some swing-related information
for the automatically generated

BeanInfo

classes.
This annotation is not used if the annotated class
has a corresponding user-defined

BeanInfo

class,
which does not imply the automatic analysis.

The

isContainer

feature attribute

was introduced primarily for the Swing library.
All Swing components extend the

Container

class by design, so the builder tool assumes that all Swing components
are containers. The

BeanInfo

classes
with the

isContainer

attribute allow to directly specify
whether a Swing component is a container or not.

**Since:** 9

@Target

(

TYPE

)

@Retention

(

RUNTIME

)
public @interface

SwingContainer

An annotation used to specify some swing-related information
for the automatically generated

BeanInfo

classes.
This annotation is not used if the annotated class
has a corresponding user-defined

BeanInfo

class,
which does not imply the automatic analysis.

The

isContainer

feature attribute

was introduced primarily for the Swing library.
All Swing components extend the

Container

class by design, so the builder tool assumes that all Swing components
are containers. The

BeanInfo

classes
with the

isContainer

attribute allow to directly specify
whether a Swing component is a container or not.

The

isContainer

feature attribute

was introduced primarily for the Swing library.
All Swing components extend the

Container

class by design, so the builder tool assumes that all Swing components
are containers. The

BeanInfo

classes
with the

isContainer

attribute allow to directly specify
whether a Swing component is a container or not.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

delegate

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

boolean

value

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

delegate

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

boolean

value

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

---

#### Optional Element Summary

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
boolean value
```

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

**Returns:** true

if the annotated class is a Swing container;

false

otherwise.

**Default:** true

- - delegate

```java
String
delegate
```

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

**Returns:** the name of the getter method in the annotated class,
which returns the corresponding Swing container,
or an empty string if the method name is not set.

**Default:** ""

Element Detail

- value

```java
boolean value
```

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

**Returns:** true

if the annotated class is a Swing container;

false

otherwise.

**Default:** true

---

#### Element Detail

value

```java
boolean value
```

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

**Returns:** true

if the annotated class is a Swing container;

false

otherwise.

**Default:** true

---

#### value

boolean value

The value that indicates whether the annotated class can be used
as a container for other Swing components or not.

- delegate

```java
String
delegate
```

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

**Returns:** the name of the getter method in the annotated class,
which returns the corresponding Swing container,
or an empty string if the method name is not set.

**Default:** ""

delegate

```java
String
delegate
```

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

**Returns:** the name of the getter method in the annotated class,
which returns the corresponding Swing container,
or an empty string if the method name is not set.

**Default:** ""

---

#### delegate

String

delegate

The name of the getter method in the annotated class,
which returns the corresponding Swing container,
if it is not recommended to add subcomponents
to the annotated class directly.

---

