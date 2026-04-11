# Annotation Type Documented

**Source:** `java.base\java\lang\annotation\Documented.html`

### Class Description

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
ANNOTATION_TYPE
)
public @interface
Documented
```

If the annotation

@Documented

is present on the declaration
of an annotation type

A

, then any

@A

annotation on
an element is considered part of the element's public contract.

In more detail, when an annotation type

A

is annotated with

Documented

, the presence and value of annotations of type

A

are a part of the public contract of the elements

A

annotates.

Conversely, if an annotation type

B

is

not

annotated with

Documented

, the presence and value of

B

annotations are

not

part of the public contract
of the elements

B

annotates.

Concretely, if an annotation type is annotated with

Documented

, by default a tool like javadoc will display
annotations of that type in its output while annotations of
annotation types without

Documented

will not be displayed.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Annotation Type Documented

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
ANNOTATION_TYPE
)
public @interface
Documented
```

If the annotation

@Documented

is present on the declaration
of an annotation type

A

, then any

@A

annotation on
an element is considered part of the element's public contract.

In more detail, when an annotation type

A

is annotated with

Documented

, the presence and value of annotations of type

A

are a part of the public contract of the elements

A

annotates.

Conversely, if an annotation type

B

is

not

annotated with

Documented

, the presence and value of

B

annotations are

not

part of the public contract
of the elements

B

annotates.

Concretely, if an annotation type is annotated with

Documented

, by default a tool like javadoc will display
annotations of that type in its output while annotations of
annotation types without

Documented

will not be displayed.

**Since:** 1.5

@Documented

@Retention

(

RUNTIME

)

@Target

(

ANNOTATION_TYPE

)
public @interface

Documented

If the annotation

@Documented

is present on the declaration
of an annotation type

A

, then any

@A

annotation on
an element is considered part of the element's public contract.

In more detail, when an annotation type

A

is annotated with

Documented

, the presence and value of annotations of type

A

are a part of the public contract of the elements

A

annotates.

Conversely, if an annotation type

B

is

not

annotated with

Documented

, the presence and value of

B

annotations are

not

part of the public contract
of the elements

B

annotates.

Concretely, if an annotation type is annotated with

Documented

, by default a tool like javadoc will display
annotations of that type in its output while annotations of
annotation types without

Documented

will not be displayed.

---

