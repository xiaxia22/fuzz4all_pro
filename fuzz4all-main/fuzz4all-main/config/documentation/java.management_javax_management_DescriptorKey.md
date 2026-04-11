# Annotation Type DescriptorKey

**Source:** `java.management\javax\management\DescriptorKey.html`

### Class Description

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
METHOD
)
public @interface
DescriptorKey
```

Meta-annotation that describes how an annotation element relates
to a field in a

Descriptor

. This can be the Descriptor for
an MBean, or for an attribute, operation, or constructor in an
MBean, or for a parameter of an operation or constructor.

Consider this annotation for example:

```java
@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();
}
```

and this use of the annotation:

```java
public interface CacheControlMBean {

@Units("bytes")

public long getCacheSize();
}
```

When a Standard MBean is made from the

CacheControlMBean

,
the usual rules mean that it will have an attribute called

CacheSize

of type

long

. The

@Units

annotation, given the above definition, will ensure that the

MBeanAttributeInfo

for this attribute will have a

Descriptor

that has a field called

units

with
corresponding value

bytes

.

Similarly, if the annotation looks like this:

```java
@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();

@DescriptorKey("descriptionResourceKey")

String resourceKey() default "";

@DescriptorKey("descriptionResourceBundleBaseName")

String resourceBundleBaseName() default "";
}
```

and it is used like this:

```java
public interface CacheControlMBean {

@Units("bytes",
resourceKey="bytes.key",
resourceBundleBaseName="com.example.foo.MBeanResources")

public long getCacheSize();
}
```

then the resulting

Descriptor

will contain the following
fields:

Descriptor Fields

Name

Value

units

"bytes"

descriptionResourceKey

"bytes.key"

descriptionResourceBundleBaseName

"com.example.foo.MBeanResources"

An annotation such as

@Units

can be applied to:

- a Standard MBean or MXBean interface;

a method in such an interface;

a parameter of a method in a Standard MBean or MXBean interface
when that method is an operation (not a getter or setter for an attribute);

a public constructor in the class that implements a Standard MBean
or MXBean;

a parameter in such a constructor.

Other uses of the annotation are ignored.

Interface annotations are checked only on the exact interface
that defines the management interface of a Standard MBean or an
MXBean, not on its parent interfaces. Method annotations are
checked only in the most specific interface in which the method
appears; in other words, if a child interface overrides a method
from a parent interface, only

@DescriptorKey

annotations in
the method in the child interface are considered.

The Descriptor fields contributed in this way by different
annotations on the same program element must be consistent. That
is, two different annotations, or two members of the same
annotation, must not define a different value for the same
Descriptor field. Fields from annotations on a getter method must
also be consistent with fields from annotations on the
corresponding setter method.

The Descriptor resulting from these annotations will be merged
with any Descriptor fields provided by the implementation, such as
the

immutableInfo

field for an MBean. The fields from the annotations
must be consistent with these fields provided by the implementation.

An annotation element to be converted into a descriptor field
can be of any type allowed by the Java language, except an annotation
or an array of annotations. The value of the field is derived from
the value of the annotation element as follows:

Descriptor Field Types

Annotation element

Descriptor field

Primitive value (

5

,

false

, etc)

Wrapped value (

Integer.valueOf(5)

,

Boolean.FALSE

, etc)

Class constant (e.g.

Thread.class

)

Class name from

Class.getName()

(e.g.

"java.lang.Thread"

)

Enum constant (e.g.

ElementType.FIELD

)

Constant name from

Enum.name()

(e.g.

"FIELD"

)

Array of class constants or enum constants

String array derived by applying these rules to each
element

Value of any other type

(

String

,

String[]

,

int[]

, etc)

The same value

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String Returns the descriptor key.

---

### Additional Sections

#### Annotation Type DescriptorKey

```java
@Documented

@Retention
(
RUNTIME
)

@Target
(
METHOD
)
public @interface
DescriptorKey
```

Meta-annotation that describes how an annotation element relates
to a field in a

Descriptor

. This can be the Descriptor for
an MBean, or for an attribute, operation, or constructor in an
MBean, or for a parameter of an operation or constructor.

Consider this annotation for example:

```java
@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();
}
```

and this use of the annotation:

```java
public interface CacheControlMBean {

@Units("bytes")

public long getCacheSize();
}
```

When a Standard MBean is made from the

CacheControlMBean

,
the usual rules mean that it will have an attribute called

CacheSize

of type

long

. The

@Units

annotation, given the above definition, will ensure that the

MBeanAttributeInfo

for this attribute will have a

Descriptor

that has a field called

units

with
corresponding value

bytes

.

Similarly, if the annotation looks like this:

```java
@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();

@DescriptorKey("descriptionResourceKey")

String resourceKey() default "";

@DescriptorKey("descriptionResourceBundleBaseName")

String resourceBundleBaseName() default "";
}
```

and it is used like this:

```java
public interface CacheControlMBean {

@Units("bytes",
resourceKey="bytes.key",
resourceBundleBaseName="com.example.foo.MBeanResources")

public long getCacheSize();
}
```

then the resulting

Descriptor

will contain the following
fields:

Descriptor Fields

Name

Value

units

"bytes"

descriptionResourceKey

"bytes.key"

descriptionResourceBundleBaseName

"com.example.foo.MBeanResources"

An annotation such as

@Units

can be applied to:

- a Standard MBean or MXBean interface;

a method in such an interface;

a parameter of a method in a Standard MBean or MXBean interface
when that method is an operation (not a getter or setter for an attribute);

a public constructor in the class that implements a Standard MBean
or MXBean;

a parameter in such a constructor.

Other uses of the annotation are ignored.

Interface annotations are checked only on the exact interface
that defines the management interface of a Standard MBean or an
MXBean, not on its parent interfaces. Method annotations are
checked only in the most specific interface in which the method
appears; in other words, if a child interface overrides a method
from a parent interface, only

@DescriptorKey

annotations in
the method in the child interface are considered.

The Descriptor fields contributed in this way by different
annotations on the same program element must be consistent. That
is, two different annotations, or two members of the same
annotation, must not define a different value for the same
Descriptor field. Fields from annotations on a getter method must
also be consistent with fields from annotations on the
corresponding setter method.

The Descriptor resulting from these annotations will be merged
with any Descriptor fields provided by the implementation, such as
the

immutableInfo

field for an MBean. The fields from the annotations
must be consistent with these fields provided by the implementation.

An annotation element to be converted into a descriptor field
can be of any type allowed by the Java language, except an annotation
or an array of annotations. The value of the field is derived from
the value of the annotation element as follows:

Descriptor Field Types

Annotation element

Descriptor field

Primitive value (

5

,

false

, etc)

Wrapped value (

Integer.valueOf(5)

,

Boolean.FALSE

, etc)

Class constant (e.g.

Thread.class

)

Class name from

Class.getName()

(e.g.

"java.lang.Thread"

)

Enum constant (e.g.

ElementType.FIELD

)

Constant name from

Enum.name()

(e.g.

"FIELD"

)

Array of class constants or enum constants

String array derived by applying these rules to each
element

Value of any other type

(

String

,

String[]

,

int[]

, etc)

The same value

**Since:** 1.6

@Documented

@Retention

(

RUNTIME

)

@Target

(

METHOD

)
public @interface

DescriptorKey

Meta-annotation that describes how an annotation element relates
to a field in a

Descriptor

. This can be the Descriptor for
an MBean, or for an attribute, operation, or constructor in an
MBean, or for a parameter of an operation or constructor.

Consider this annotation for example:

```java
@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();
}
```

and this use of the annotation:

```java
public interface CacheControlMBean {

@Units("bytes")

public long getCacheSize();
}
```

When a Standard MBean is made from the

CacheControlMBean

,
the usual rules mean that it will have an attribute called

CacheSize

of type

long

. The

@Units

annotation, given the above definition, will ensure that the

MBeanAttributeInfo

for this attribute will have a

Descriptor

that has a field called

units

with
corresponding value

bytes

.

Similarly, if the annotation looks like this:

```java
@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();

@DescriptorKey("descriptionResourceKey")

String resourceKey() default "";

@DescriptorKey("descriptionResourceBundleBaseName")

String resourceBundleBaseName() default "";
}
```

and it is used like this:

```java
public interface CacheControlMBean {

@Units("bytes",
resourceKey="bytes.key",
resourceBundleBaseName="com.example.foo.MBeanResources")

public long getCacheSize();
}
```

then the resulting

Descriptor

will contain the following
fields:

Descriptor Fields

Name

Value

units

"bytes"

descriptionResourceKey

"bytes.key"

descriptionResourceBundleBaseName

"com.example.foo.MBeanResources"

An annotation such as

@Units

can be applied to:

- a Standard MBean or MXBean interface;

a method in such an interface;

a parameter of a method in a Standard MBean or MXBean interface
when that method is an operation (not a getter or setter for an attribute);

a public constructor in the class that implements a Standard MBean
or MXBean;

a parameter in such a constructor.

Other uses of the annotation are ignored.

Interface annotations are checked only on the exact interface
that defines the management interface of a Standard MBean or an
MXBean, not on its parent interfaces. Method annotations are
checked only in the most specific interface in which the method
appears; in other words, if a child interface overrides a method
from a parent interface, only

@DescriptorKey

annotations in
the method in the child interface are considered.

The Descriptor fields contributed in this way by different
annotations on the same program element must be consistent. That
is, two different annotations, or two members of the same
annotation, must not define a different value for the same
Descriptor field. Fields from annotations on a getter method must
also be consistent with fields from annotations on the
corresponding setter method.

The Descriptor resulting from these annotations will be merged
with any Descriptor fields provided by the implementation, such as
the

immutableInfo

field for an MBean. The fields from the annotations
must be consistent with these fields provided by the implementation.

An annotation element to be converted into a descriptor field
can be of any type allowed by the Java language, except an annotation
or an array of annotations. The value of the field is derived from
the value of the annotation element as follows:

Descriptor Field Types

Annotation element

Descriptor field

Primitive value (

5

,

false

, etc)

Wrapped value (

Integer.valueOf(5)

,

Boolean.FALSE

, etc)

Class constant (e.g.

Thread.class

)

Class name from

Class.getName()

(e.g.

"java.lang.Thread"

)

Enum constant (e.g.

ElementType.FIELD

)

Constant name from

Enum.name()

(e.g.

"FIELD"

)

Array of class constants or enum constants

String array derived by applying these rules to each
element

Value of any other type

(

String

,

String[]

,

int[]

, etc)

The same value

Meta-annotation that describes how an annotation element relates
to a field in a

Descriptor

. This can be the Descriptor for
an MBean, or for an attribute, operation, or constructor in an
MBean, or for a parameter of an operation or constructor.

Consider this annotation for example:

@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();
}

and this use of the annotation:

public interface CacheControlMBean {

@Units("bytes")

public long getCacheSize();
}

When a Standard MBean is made from the

CacheControlMBean

,
the usual rules mean that it will have an attribute called

CacheSize

of type

long

. The

@Units

annotation, given the above definition, will ensure that the

MBeanAttributeInfo

for this attribute will have a

Descriptor

that has a field called

units

with
corresponding value

bytes

.

Similarly, if the annotation looks like this:

@Documented
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface Units {

@DescriptorKey("units")

String value();

@DescriptorKey("descriptionResourceKey")

String resourceKey() default "";

@DescriptorKey("descriptionResourceBundleBaseName")

String resourceBundleBaseName() default "";
}

and it is used like this:

public interface CacheControlMBean {

@Units("bytes",
resourceKey="bytes.key",
resourceBundleBaseName="com.example.foo.MBeanResources")

public long getCacheSize();
}

then the resulting

Descriptor

will contain the following
fields:

An annotation such as

@Units

can be applied to:

a Standard MBean or MXBean interface;

a method in such an interface;

a parameter of a method in a Standard MBean or MXBean interface
when that method is an operation (not a getter or setter for an attribute);

a public constructor in the class that implements a Standard MBean
or MXBean;

a parameter in such a constructor.

Other uses of the annotation are ignored.

Interface annotations are checked only on the exact interface
that defines the management interface of a Standard MBean or an
MXBean, not on its parent interfaces. Method annotations are
checked only in the most specific interface in which the method
appears; in other words, if a child interface overrides a method
from a parent interface, only

@DescriptorKey

annotations in
the method in the child interface are considered.

The Descriptor fields contributed in this way by different
annotations on the same program element must be consistent. That
is, two different annotations, or two members of the same
annotation, must not define a different value for the same
Descriptor field. Fields from annotations on a getter method must
also be consistent with fields from annotations on the
corresponding setter method.

The Descriptor resulting from these annotations will be merged
with any Descriptor fields provided by the implementation, such as
the

immutableInfo

field for an MBean. The fields from the annotations
must be consistent with these fields provided by the implementation.

An annotation element to be converted into a descriptor field
can be of any type allowed by the Java language, except an annotation
or an array of annotations. The value of the field is derived from
the value of the annotation element as follows:

Descriptor Field Types

Annotation element

Descriptor field

Primitive value (

5

,

false

, etc)

Wrapped value (

Integer.valueOf(5)

,

Boolean.FALSE

, etc)

Class constant (e.g.

Thread.class

)

Class name from

Class.getName()

(e.g.

"java.lang.Thread"

)

Enum constant (e.g.

ElementType.FIELD

)

Constant name from

Enum.name()

(e.g.

"FIELD"

)

Array of class constants or enum constants

String array derived by applying these rules to each
element

Value of any other type

(

String

,

String[]

,

int[]

, etc)

The same value

The Descriptor fields contributed in this way by different
annotations on the same program element must be consistent. That
is, two different annotations, or two members of the same
annotation, must not define a different value for the same
Descriptor field. Fields from annotations on a getter method must
also be consistent with fields from annotations on the
corresponding setter method.

The Descriptor resulting from these annotations will be merged
with any Descriptor fields provided by the implementation, such as
the

immutableInfo

field for an MBean. The fields from the annotations
must be consistent with these fields provided by the implementation.

An annotation element to be converted into a descriptor field
can be of any type allowed by the Java language, except an annotation
or an array of annotations. The value of the field is derived from
the value of the annotation element as follows:

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

value

Returns the descriptor key.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

value

Returns the descriptor key.

---

#### Required Element Summary

Returns the descriptor key.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

Returns the descriptor key.

**Returns:** the descriptor key

Element Detail

- value

```java
String
value
```

Returns the descriptor key.

**Returns:** the descriptor key

---

#### Element Detail

value

```java
String
value
```

Returns the descriptor key.

**Returns:** the descriptor key

---

#### value

String

value

Returns the descriptor key.

---

