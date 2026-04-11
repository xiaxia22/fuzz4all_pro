# Annotation Type BeanProperty

**Source:** `java.desktop\java\beans\BeanProperty.html`

### Class Description

```java
@Documented

@Target
(
METHOD
)

@Retention
(
RUNTIME
)
public @interface
BeanProperty
```

An annotation used to specify some property-related information for the
automatically generated

BeanInfo

classes. This annotation is not used
if the annotated class has a corresponding user-defined

BeanInfo

class, which does not imply the automatic analysis. If both the read and the
write methods of the property are annotated, then the read method annotation
will have more priority and replace the write method annotation.

**Since:** 9
**See Also:** BeanInfo.getPropertyDescriptors()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### bound

boolean The value that indicates whether the annotated property can be
a bound property or not.

---

#### description

String The short description for the descriptor of the annotated property.

---

#### enumerationValues

String [] The array of names for the public static fields
that contains the valid values of the annotated property.

---

#### expert

boolean The value that indicates whether the annotated property is
an expert property or not.

---

#### hidden

boolean The value that indicates whether the annotated property is
a hidden property or not.

---

#### preferred

boolean The value that indicates whether the annotated property is
a preferred property or not.

---

#### required

boolean The value that indicates whether the annotated property is
a required property or not.

---

#### visualUpdate

boolean The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

---

### Additional Sections

#### Annotation Type BeanProperty

```java
@Documented

@Target
(
METHOD
)

@Retention
(
RUNTIME
)
public @interface
BeanProperty
```

An annotation used to specify some property-related information for the
automatically generated

BeanInfo

classes. This annotation is not used
if the annotated class has a corresponding user-defined

BeanInfo

class, which does not imply the automatic analysis. If both the read and the
write methods of the property are annotated, then the read method annotation
will have more priority and replace the write method annotation.

**Since:** 9
**See Also:** BeanInfo.getPropertyDescriptors()

@Documented

@Target

(

METHOD

)

@Retention

(

RUNTIME

)
public @interface

BeanProperty

An annotation used to specify some property-related information for the
automatically generated

BeanInfo

classes. This annotation is not used
if the annotated class has a corresponding user-defined

BeanInfo

class, which does not imply the automatic analysis. If both the read and the
write methods of the property are annotated, then the read method annotation
will have more priority and replace the write method annotation.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

bound

The value that indicates whether the annotated property can be
a

bound

property or not.

String

description

The

short description

for the

descriptor

of the annotated property.

String

[]

enumerationValues

The array of names for the public static fields
that contains the valid values of the annotated property.

boolean

expert

The value that indicates whether the annotated property is
an

expert

property or not.

boolean

hidden

The value that indicates whether the annotated property is
a

hidden

property or not.

boolean

preferred

The value that indicates whether the annotated property is
a

preferred

property or not.

boolean

required

The value that indicates whether the annotated property is
a required property or not.

boolean

visualUpdate

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

bound

The value that indicates whether the annotated property can be
a

bound

property or not.

String

description

The

short description

for the

descriptor

of the annotated property.

String

[]

enumerationValues

The array of names for the public static fields
that contains the valid values of the annotated property.

boolean

expert

The value that indicates whether the annotated property is
an

expert

property or not.

boolean

hidden

The value that indicates whether the annotated property is
a

hidden

property or not.

boolean

preferred

The value that indicates whether the annotated property is
a

preferred

property or not.

boolean

required

The value that indicates whether the annotated property is
a required property or not.

boolean

visualUpdate

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

---

#### Optional Element Summary

The value that indicates whether the annotated property can be
a

bound

property or not.

The

short description

for the

descriptor

of the annotated property.

The array of names for the public static fields
that contains the valid values of the annotated property.

The value that indicates whether the annotated property is
an

expert

property or not.

The value that indicates whether the annotated property is
a

hidden

property or not.

The value that indicates whether the annotated property is
a

preferred

property or not.

The value that indicates whether the annotated property is
a required property or not.

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- bound

```java
boolean bound
```

The value that indicates whether the annotated property can be
a

bound

property or not.
This value applies only to the beans that have the

propertyChange

event set.

**Returns:** true

if the annotated property can be a bound property;

false

otherwise.

**Default:** true

- - expert

```java
boolean expert
```

The value that indicates whether the annotated property is
an

expert

property or not.

**Returns:** true

if the annotated property is an expert property;

false

otherwise.

**Default:** false

- - hidden

```java
boolean hidden
```

The value that indicates whether the annotated property is
a

hidden

property or not.

**Returns:** true

if the annotated property is a hidden property;

false

otherwise.

**Default:** false

- - preferred

```java
boolean preferred
```

The value that indicates whether the annotated property is
a

preferred

property or not.

**Returns:** true

if the annotated property is a preferred property;

false

otherwise.

**Default:** false

- - required

```java
boolean required
```

The value that indicates whether the annotated property is
a required property or not.

**Returns:** true

if the annotated property is a required property;

false

otherwise.

**Default:** false

- - visualUpdate

```java
boolean visualUpdate
```

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

**Returns:** true

if the corresponding component is repainted;

false

otherwise.

**Default:** false

- - description

```java
String
description
```

The

short description

for the

descriptor

of the annotated property.

**Returns:** the property description,
or an empty string if the description is not set.

**Default:** ""

- - enumerationValues

```java
String
[] enumerationValues
```

The array of names for the public static fields
that contains the valid values of the annotated property.
These names are used to generate the

enumerationValues

feature attribute

that must contain the following items per each property value:
a displayable name for the property value, the actual property value,
and a Java code piece used for the code generator.

**Returns:** the names of the valid values of the annotated property,
or an empty array if the names are not provided.

**Default:** {}

Element Detail

- bound

```java
boolean bound
```

The value that indicates whether the annotated property can be
a

bound

property or not.
This value applies only to the beans that have the

propertyChange

event set.

**Returns:** true

if the annotated property can be a bound property;

false

otherwise.

**Default:** true

---

#### Element Detail

bound

```java
boolean bound
```

The value that indicates whether the annotated property can be
a

bound

property or not.
This value applies only to the beans that have the

propertyChange

event set.

**Returns:** true

if the annotated property can be a bound property;

false

otherwise.

**Default:** true

---

#### bound

boolean bound

The value that indicates whether the annotated property can be
a

bound

property or not.
This value applies only to the beans that have the

propertyChange

event set.

- expert

```java
boolean expert
```

The value that indicates whether the annotated property is
an

expert

property or not.

**Returns:** true

if the annotated property is an expert property;

false

otherwise.

**Default:** false

expert

```java
boolean expert
```

The value that indicates whether the annotated property is
an

expert

property or not.

**Returns:** true

if the annotated property is an expert property;

false

otherwise.

**Default:** false

---

#### expert

boolean expert

The value that indicates whether the annotated property is
an

expert

property or not.

- hidden

```java
boolean hidden
```

The value that indicates whether the annotated property is
a

hidden

property or not.

**Returns:** true

if the annotated property is a hidden property;

false

otherwise.

**Default:** false

hidden

```java
boolean hidden
```

The value that indicates whether the annotated property is
a

hidden

property or not.

**Returns:** true

if the annotated property is a hidden property;

false

otherwise.

**Default:** false

---

#### hidden

boolean hidden

The value that indicates whether the annotated property is
a

hidden

property or not.

- preferred

```java
boolean preferred
```

The value that indicates whether the annotated property is
a

preferred

property or not.

**Returns:** true

if the annotated property is a preferred property;

false

otherwise.

**Default:** false

preferred

```java
boolean preferred
```

The value that indicates whether the annotated property is
a

preferred

property or not.

**Returns:** true

if the annotated property is a preferred property;

false

otherwise.

**Default:** false

---

#### preferred

boolean preferred

The value that indicates whether the annotated property is
a

preferred

property or not.

- required

```java
boolean required
```

The value that indicates whether the annotated property is
a required property or not.

**Returns:** true

if the annotated property is a required property;

false

otherwise.

**Default:** false

required

```java
boolean required
```

The value that indicates whether the annotated property is
a required property or not.

**Returns:** true

if the annotated property is a required property;

false

otherwise.

**Default:** false

---

#### required

boolean required

The value that indicates whether the annotated property is
a required property or not.

- visualUpdate

```java
boolean visualUpdate
```

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

**Returns:** true

if the corresponding component is repainted;

false

otherwise.

**Default:** false

visualUpdate

```java
boolean visualUpdate
```

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

**Returns:** true

if the corresponding component is repainted;

false

otherwise.

**Default:** false

---

#### visualUpdate

boolean visualUpdate

The value that indicates whether the corresponding component
is repainted after the annotated property got changed or not.

- description

```java
String
description
```

The

short description

for the

descriptor

of the annotated property.

**Returns:** the property description,
or an empty string if the description is not set.

**Default:** ""

description

```java
String
description
```

The

short description

for the

descriptor

of the annotated property.

**Returns:** the property description,
or an empty string if the description is not set.

**Default:** ""

---

#### description

String

description

The

short description

for the

descriptor

of the annotated property.

- enumerationValues

```java
String
[] enumerationValues
```

The array of names for the public static fields
that contains the valid values of the annotated property.
These names are used to generate the

enumerationValues

feature attribute

that must contain the following items per each property value:
a displayable name for the property value, the actual property value,
and a Java code piece used for the code generator.

**Returns:** the names of the valid values of the annotated property,
or an empty array if the names are not provided.

**Default:** {}

enumerationValues

```java
String
[] enumerationValues
```

The array of names for the public static fields
that contains the valid values of the annotated property.
These names are used to generate the

enumerationValues

feature attribute

that must contain the following items per each property value:
a displayable name for the property value, the actual property value,
and a Java code piece used for the code generator.

**Returns:** the names of the valid values of the annotated property,
or an empty array if the names are not provided.

**Default:** {}

---

#### enumerationValues

String

[] enumerationValues

The array of names for the public static fields
that contains the valid values of the annotated property.
These names are used to generate the

enumerationValues

feature attribute

that must contain the following items per each property value:
a displayable name for the property value, the actual property value,
and a Java code piece used for the code generator.

---

