# Annotation Type Transient

**Source:** `java.desktop\java\beans\Transient.html`

### Class Description

```java
@Target
(
METHOD
)

@Retention
(
RUNTIME
)
public @interface
Transient
```

Indicates that an attribute called "transient"
should be declared with the given

value

when the

Introspector

constructs
a

PropertyDescriptor

or

EventSetDescriptor

classes associated with the annotated code element.
A

true

value for the "transient" attribute
indicates to encoders derived from

Encoder

that this feature should be ignored.

The

Transient

annotation may be used
in any of the methods that are involved
in a

FeatureDescriptor

subclass
to identify the transient feature in the annotated class and its subclasses.
Normally, the method that starts with "get" is the best place
to put the annotation and it is this declaration
that takes precedence in the case of multiple annotations
being defined for the same feature.

To declare a feature non-transient in a class
whose superclass declares it transient,
use

@Transient(false)

.
In all cases, the

Introspector

decides
if a feature is transient by referring to the annotation
on the most specific superclass.
If no

Transient

annotation is present
in any superclass the feature is not transient.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

boolean Returns whether or not the Introspector should
construct artifacts for the annotated method.

---

### Additional Sections

#### Annotation Type Transient

```java
@Target
(
METHOD
)

@Retention
(
RUNTIME
)
public @interface
Transient
```

Indicates that an attribute called "transient"
should be declared with the given

value

when the

Introspector

constructs
a

PropertyDescriptor

or

EventSetDescriptor

classes associated with the annotated code element.
A

true

value for the "transient" attribute
indicates to encoders derived from

Encoder

that this feature should be ignored.

The

Transient

annotation may be used
in any of the methods that are involved
in a

FeatureDescriptor

subclass
to identify the transient feature in the annotated class and its subclasses.
Normally, the method that starts with "get" is the best place
to put the annotation and it is this declaration
that takes precedence in the case of multiple annotations
being defined for the same feature.

To declare a feature non-transient in a class
whose superclass declares it transient,
use

@Transient(false)

.
In all cases, the

Introspector

decides
if a feature is transient by referring to the annotation
on the most specific superclass.
If no

Transient

annotation is present
in any superclass the feature is not transient.

**Since:** 1.7

@Target

(

METHOD

)

@Retention

(

RUNTIME

)
public @interface

Transient

Indicates that an attribute called "transient"
should be declared with the given

value

when the

Introspector

constructs
a

PropertyDescriptor

or

EventSetDescriptor

classes associated with the annotated code element.
A

true

value for the "transient" attribute
indicates to encoders derived from

Encoder

that this feature should be ignored.

The

Transient

annotation may be used
in any of the methods that are involved
in a

FeatureDescriptor

subclass
to identify the transient feature in the annotated class and its subclasses.
Normally, the method that starts with "get" is the best place
to put the annotation and it is this declaration
that takes precedence in the case of multiple annotations
being defined for the same feature.

To declare a feature non-transient in a class
whose superclass declares it transient,
use

@Transient(false)

.
In all cases, the

Introspector

decides
if a feature is transient by referring to the annotation
on the most specific superclass.
If no

Transient

annotation is present
in any superclass the feature is not transient.

The

Transient

annotation may be used
in any of the methods that are involved
in a

FeatureDescriptor

subclass
to identify the transient feature in the annotated class and its subclasses.
Normally, the method that starts with "get" is the best place
to put the annotation and it is this declaration
that takes precedence in the case of multiple annotations
being defined for the same feature.

To declare a feature non-transient in a class
whose superclass declares it transient,
use

@Transient(false)

.
In all cases, the

Introspector

decides
if a feature is transient by referring to the annotation
on the most specific superclass.
If no

Transient

annotation is present
in any superclass the feature is not transient.

To declare a feature non-transient in a class
whose superclass declares it transient,
use

@Transient(false)

.
In all cases, the

Introspector

decides
if a feature is transient by referring to the annotation
on the most specific superclass.
If no

Transient

annotation is present
in any superclass the feature is not transient.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

---

#### Optional Element Summary

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
boolean value
```

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

**Returns:** whether or not the

Introspector

should
construct artifacts for the annotated method

**Default:** true

Element Detail

- value

```java
boolean value
```

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

**Returns:** whether or not the

Introspector

should
construct artifacts for the annotated method

**Default:** true

---

#### Element Detail

value

```java
boolean value
```

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

**Returns:** whether or not the

Introspector

should
construct artifacts for the annotated method

**Default:** true

---

#### value

boolean value

Returns whether or not the

Introspector

should
construct artifacts for the annotated method.

---

