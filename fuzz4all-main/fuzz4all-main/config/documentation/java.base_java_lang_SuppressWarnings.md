# Annotation Type SuppressWarnings

**Source:** `java.base\java\lang\SuppressWarnings.html`

### Class Description

```java
@Target
({
TYPE
,
FIELD
,
METHOD
,
PARAMETER
,
CONSTRUCTOR
,
LOCAL_VARIABLE
,
MODULE
})

@Retention
(
SOURCE
)
public @interface
SuppressWarnings
```

Indicates that the named compiler warnings should be suppressed in the
annotated element (and in all program elements contained in the annotated
element). Note that the set of warnings suppressed in a given element is
a superset of the warnings suppressed in all containing elements. For
example, if you annotate a class to suppress one warning and annotate a
method to suppress another, both warnings will be suppressed in the method.
However, note that if a warning is suppressed in a

module-info

file, the suppression applies to elements within the
file and

not

to types contained within the module.

As a matter of style, programmers should always use this annotation
on the most deeply nested element where it is effective. If you want to
suppress a warning in a particular method, you should annotate that
method rather than its class.

**Since:** 1.5
**See The Java™ Language Specification :** 4.8 Raw Types, 4.12.2 Variables of Reference Type, 5.1.9 Unchecked Conversion, 5.5.2 Checked Casts and Unchecked Casts, 9.6.4.5 @SuppressWarnings

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String [] The set of warnings that are to be suppressed by the compiler in the
annotated element.

---

### Additional Sections

#### Annotation Type SuppressWarnings

```java
@Target
({
TYPE
,
FIELD
,
METHOD
,
PARAMETER
,
CONSTRUCTOR
,
LOCAL_VARIABLE
,
MODULE
})

@Retention
(
SOURCE
)
public @interface
SuppressWarnings
```

Indicates that the named compiler warnings should be suppressed in the
annotated element (and in all program elements contained in the annotated
element). Note that the set of warnings suppressed in a given element is
a superset of the warnings suppressed in all containing elements. For
example, if you annotate a class to suppress one warning and annotate a
method to suppress another, both warnings will be suppressed in the method.
However, note that if a warning is suppressed in a

module-info

file, the suppression applies to elements within the
file and

not

to types contained within the module.

As a matter of style, programmers should always use this annotation
on the most deeply nested element where it is effective. If you want to
suppress a warning in a particular method, you should annotate that
method rather than its class.

**Since:** 1.5
**See The Java™ Language Specification :** 4.8 Raw Types, 4.12.2 Variables of Reference Type, 5.1.9 Unchecked Conversion, 5.5.2 Checked Casts and Unchecked Casts, 9.6.4.5 @SuppressWarnings

@Target

({

TYPE

,

FIELD

,

METHOD

,

PARAMETER

,

CONSTRUCTOR

,

LOCAL_VARIABLE

,

MODULE

})

@Retention

(

SOURCE

)
public @interface

SuppressWarnings

Indicates that the named compiler warnings should be suppressed in the
annotated element (and in all program elements contained in the annotated
element). Note that the set of warnings suppressed in a given element is
a superset of the warnings suppressed in all containing elements. For
example, if you annotate a class to suppress one warning and annotate a
method to suppress another, both warnings will be suppressed in the method.
However, note that if a warning is suppressed in a

module-info

file, the suppression applies to elements within the
file and

not

to types contained within the module.

As a matter of style, programmers should always use this annotation
on the most deeply nested element where it is effective. If you want to
suppress a warning in a particular method, you should annotate that
method rather than its class.

As a matter of style, programmers should always use this annotation
on the most deeply nested element where it is effective. If you want to
suppress a warning in a particular method, you should annotate that
method rather than its class.

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

The set of warnings that are to be suppressed by the compiler in the
annotated element.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

The set of warnings that are to be suppressed by the compiler in the
annotated element.

---

#### Required Element Summary

The set of warnings that are to be suppressed by the compiler in the
annotated element.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
[] value
```

The set of warnings that are to be suppressed by the compiler in the
annotated element. Duplicate names are permitted. The second and
successive occurrences of a name are ignored. The presence of
unrecognized warning names is

not

an error: Compilers must
ignore any warning names they do not recognize. They are, however,
free to emit a warning if an annotation contains an unrecognized
warning name.

The string

"unchecked"

is used to suppress
unchecked warnings. Compiler vendors should document the
additional warning names they support in conjunction with this
annotation type. They are encouraged to cooperate to ensure
that the same names work across multiple compilers.

**Returns:** the set of warnings to be suppressed

Element Detail

- value

```java
String
[] value
```

The set of warnings that are to be suppressed by the compiler in the
annotated element. Duplicate names are permitted. The second and
successive occurrences of a name are ignored. The presence of
unrecognized warning names is

not

an error: Compilers must
ignore any warning names they do not recognize. They are, however,
free to emit a warning if an annotation contains an unrecognized
warning name.

The string

"unchecked"

is used to suppress
unchecked warnings. Compiler vendors should document the
additional warning names they support in conjunction with this
annotation type. They are encouraged to cooperate to ensure
that the same names work across multiple compilers.

**Returns:** the set of warnings to be suppressed

---

#### Element Detail

value

```java
String
[] value
```

The set of warnings that are to be suppressed by the compiler in the
annotated element. Duplicate names are permitted. The second and
successive occurrences of a name are ignored. The presence of
unrecognized warning names is

not

an error: Compilers must
ignore any warning names they do not recognize. They are, however,
free to emit a warning if an annotation contains an unrecognized
warning name.

The string

"unchecked"

is used to suppress
unchecked warnings. Compiler vendors should document the
additional warning names they support in conjunction with this
annotation type. They are encouraged to cooperate to ensure
that the same names work across multiple compilers.

**Returns:** the set of warnings to be suppressed

---

#### value

String

[] value

The set of warnings that are to be suppressed by the compiler in the
annotated element. Duplicate names are permitted. The second and
successive occurrences of a name are ignored. The presence of
unrecognized warning names is

not

an error: Compilers must
ignore any warning names they do not recognize. They are, however,
free to emit a warning if an annotation contains an unrecognized
warning name.

The string

"unchecked"

is used to suppress
unchecked warnings. Compiler vendors should document the
additional warning names they support in conjunction with this
annotation type. They are encouraged to cooperate to ensure
that the same names work across multiple compilers.

The string

"unchecked"

is used to suppress
unchecked warnings. Compiler vendors should document the
additional warning names they support in conjunction with this
annotation type. They are encouraged to cooperate to ensure
that the same names work across multiple compilers.

---

