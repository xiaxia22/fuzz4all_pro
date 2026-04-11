# Annotation Type JavaBean

**Source:** `java.desktop\java\beans\JavaBean.html`

### Class Description

```java
@Documented

@Target
(
TYPE
)

@Retention
(
RUNTIME
)
public @interface
JavaBean
```

An annotation used to specify some class-related information
for the automatically generated

BeanInfo

classes.
This annotation is not used if the annotated class
has a corresponding user-defined

BeanInfo

class,
which does not imply the automatic analysis.

**Since:** 9
**See Also:** BeanInfo.getBeanDescriptor()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### defaultEventSet

String The name of the default event set is used to calculate its index in the array of event sets
defined in the annotated class.

---

#### defaultProperty

String The name of the default property is used to calculate its index in the array of properties
defined in the annotated class.

---

#### description

String The short description for the bean descriptor of the annotated class.

---

### Additional Sections

#### Annotation Type JavaBean

```java
@Documented

@Target
(
TYPE
)

@Retention
(
RUNTIME
)
public @interface
JavaBean
```

An annotation used to specify some class-related information
for the automatically generated

BeanInfo

classes.
This annotation is not used if the annotated class
has a corresponding user-defined

BeanInfo

class,
which does not imply the automatic analysis.

**Since:** 9
**See Also:** BeanInfo.getBeanDescriptor()

@Documented

@Target

(

TYPE

)

@Retention

(

RUNTIME

)
public @interface

JavaBean

An annotation used to specify some class-related information
for the automatically generated

BeanInfo

classes.
This annotation is not used if the annotated class
has a corresponding user-defined

BeanInfo

class,
which does not imply the automatic analysis.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

defaultEventSet

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class.

String

defaultProperty

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class.

String

description

The

short description

for the

bean descriptor

of the annotated class.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

defaultEventSet

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class.

String

defaultProperty

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class.

String

description

The

short description

for the

bean descriptor

of the annotated class.

---

#### Optional Element Summary

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class.

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class.

The

short description

for the

bean descriptor

of the annotated class.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- description

```java
String
description
```

The

short description

for the

bean descriptor

of the annotated class.

**Returns:** the bean description,
or an empty string if the description is not set.

**Default:** ""

- - defaultProperty

```java
String
defaultProperty
```

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class. If the name is not set or
the annotated class does not define a property
with the specified name, the default property index
will be calculated automatically by the

Introspector

depending on its state.

**Default:** ""

- - defaultEventSet

```java
String
defaultEventSet
```

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class. If the name is not set or
the annotated class does not define an event set
with the specified name, the default event set index
will be calculated automatically by the

Introspector

depending on its state.

**Returns:** the name of the default event set,
or an empty string if the name is not set.

**Default:** ""

Element Detail

- description

```java
String
description
```

The

short description

for the

bean descriptor

of the annotated class.

**Returns:** the bean description,
or an empty string if the description is not set.

**Default:** ""

---

#### Element Detail

description

```java
String
description
```

The

short description

for the

bean descriptor

of the annotated class.

**Returns:** the bean description,
or an empty string if the description is not set.

**Default:** ""

---

#### description

String

description

The

short description

for the

bean descriptor

of the annotated class.

- defaultProperty

```java
String
defaultProperty
```

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class. If the name is not set or
the annotated class does not define a property
with the specified name, the default property index
will be calculated automatically by the

Introspector

depending on its state.

**Default:** ""

defaultProperty

```java
String
defaultProperty
```

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class. If the name is not set or
the annotated class does not define a property
with the specified name, the default property index
will be calculated automatically by the

Introspector

depending on its state.

**Default:** ""

---

#### defaultProperty

String

defaultProperty

The name of the default property is used to calculate its

index

in the

array

of properties
defined in the annotated class. If the name is not set or
the annotated class does not define a property
with the specified name, the default property index
will be calculated automatically by the

Introspector

depending on its state.

- defaultEventSet

```java
String
defaultEventSet
```

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class. If the name is not set or
the annotated class does not define an event set
with the specified name, the default event set index
will be calculated automatically by the

Introspector

depending on its state.

**Returns:** the name of the default event set,
or an empty string if the name is not set.

**Default:** ""

defaultEventSet

```java
String
defaultEventSet
```

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class. If the name is not set or
the annotated class does not define an event set
with the specified name, the default event set index
will be calculated automatically by the

Introspector

depending on its state.

**Returns:** the name of the default event set,
or an empty string if the name is not set.

**Default:** ""

---

#### defaultEventSet

String

defaultEventSet

The name of the default event set is used to calculate its

index

in the

array

of event sets
defined in the annotated class. If the name is not set or
the annotated class does not define an event set
with the specified name, the default event set index
will be calculated automatically by the

Introspector

depending on its state.

---

