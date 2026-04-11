# Class JobName

**Source:** `java.desktop\javax\print\attribute\standard\JobName.html`

### Class Description

```java
public final class
JobName

extends
TextSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobName

is a printing attribute class, a text attribute, that
specifies the name of a print job. A job's name is an arbitrary string
defined by the client. It does not need to be unique between different jobs.
A Print Job's

JobName

attribute is set to the value supplied by the
client in the Print Request's attribute set. If, however, the client does not
supply a

JobName

attribute in the Print Request, the printer, when it
creates the Print Job, must generate a

JobName

. The printer should
generate the value of the Print Job's

JobName

attribute from the
first of the following sources that produces a value: (1) the

DocumentName

attribute of the first (or only) doc in the
job, (2) the

URL

of the first (or only) doc in the job, if the doc's
print data representation object is a

URL

, or (3) any other piece of
Print Job specific and/or document content information.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobName​(
String
jobName,

Locale
locale)

Constructs a new job name attribute with the given job name and locale.

**Parameters:**
- jobName

- job name
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

jobName

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this job name attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

JobName

.

This job name attribute's underlying string and

object

's
underlying string are equal.

This job name attribute's locale and

object

's locale are
equal.

**Overrides:**
- equals

in class

TextSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this job name
attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobName

, the category is class

JobName

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

JobName

, the category name is

"job-name"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobName

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.JobName

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.JobName

javax.print.attribute.standard.JobName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
JobName

extends
TextSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobName

is a printing attribute class, a text attribute, that
specifies the name of a print job. A job's name is an arbitrary string
defined by the client. It does not need to be unique between different jobs.
A Print Job's

JobName

attribute is set to the value supplied by the
client in the Print Request's attribute set. If, however, the client does not
supply a

JobName

attribute in the Print Request, the printer, when it
creates the Print Job, must generate a

JobName

. The printer should
generate the value of the Print Job's

JobName

attribute from the
first of the following sources that produces a value: (1) the

DocumentName

attribute of the first (or only) doc in the
job, (2) the

URL

of the first (or only) doc in the job, if the doc's
print data representation object is a

URL

, or (3) any other piece of
Print Job specific and/or document content information.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

JobName

extends

TextSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

JobName

is a printing attribute class, a text attribute, that
specifies the name of a print job. A job's name is an arbitrary string
defined by the client. It does not need to be unique between different jobs.
A Print Job's

JobName

attribute is set to the value supplied by the
client in the Print Request's attribute set. If, however, the client does not
supply a

JobName

attribute in the Print Request, the printer, when it
creates the Print Job, must generate a

JobName

. The printer should
generate the value of the Print Job's

JobName

attribute from the
first of the following sources that produces a value: (1) the

DocumentName

attribute of the first (or only) doc in the
job, (2) the

URL

of the first (or only) doc in the job, if the doc's
print data representation object is a

URL

, or (3) any other piece of
Print Job specific and/or document content information.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JobName

​(

String

jobName,

Locale

locale)

Constructs a new job name attribute with the given job name and locale.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this job name attribute is equivalent to the passed in
object.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

- Methods declared in class javax.print.attribute.

TextSyntax

getLocale

,

getValue

,

hashCode

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

Constructor Summary

Constructors

Constructor

Description

JobName

​(

String

jobName,

Locale

locale)

Constructs a new job name attribute with the given job name and locale.

---

#### Constructor Summary

Constructs a new job name attribute with the given job name and locale.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this job name attribute is equivalent to the passed in
object.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

- Methods declared in class javax.print.attribute.

TextSyntax

getLocale

,

getValue

,

hashCode

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

Returns whether this job name attribute is equivalent to the passed in
object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

TextSyntax

getLocale

,

getValue

,

hashCode

,

toString

---

#### Methods declared in class javax.print.attribute. TextSyntax

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

- JobName

```java
public JobName​(
String
jobName,

Locale
locale)
```

Constructs a new job name attribute with the given job name and locale.

**Parameters:** jobName

- job name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

jobName

is

null

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job name attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

JobName

.

This job name attribute's underlying string and

object

's
underlying string are equal.

This job name attribute's locale and

object

's locale are
equal.

**Overrides:** equals

in class

TextSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this job name
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobName

, the category is class

JobName

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

JobName

, the category name is

"job-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobName

```java
public JobName​(
String
jobName,

Locale
locale)
```

Constructs a new job name attribute with the given job name and locale.

**Parameters:** jobName

- job name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

jobName

is

null

---

#### Constructor Detail

JobName

```java
public JobName​(
String
jobName,

Locale
locale)
```

Constructs a new job name attribute with the given job name and locale.

**Parameters:** jobName

- job name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

jobName

is

null

---

#### JobName

public JobName​(

String

jobName,

Locale

locale)

Constructs a new job name attribute with the given job name and locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job name attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

JobName

.

This job name attribute's underlying string and

object

's
underlying string are equal.

This job name attribute's locale and

object

's locale are
equal.

**Overrides:** equals

in class

TextSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this job name
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobName

, the category is class

JobName

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

JobName

, the category name is

"job-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job name attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

JobName

.

This job name attribute's underlying string and

object

's
underlying string are equal.

This job name attribute's locale and

object

's locale are
equal.

**Overrides:** equals

in class

TextSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this job name
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Returns whether this job name attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

JobName

.

This job name attribute's underlying string and

object

's
underlying string are equal.

This job name attribute's locale and

object

's locale are
equal.

object

is not

null

.

object

is an instance of class

JobName

.

This job name attribute's underlying string and

object

's
underlying string are equal.

This job name attribute's locale and

object

's locale are
equal.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobName

, the category is class

JobName

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

JobName

, the category is class

JobName

itself.

For class

JobName

, the category is class

JobName

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

JobName

, the category name is

"job-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

JobName

, the category name is

"job-name"

.

For class

JobName

, the category name is

"job-name"

.

---

