# Annotation Type Category

**Source:** `jdk.jfr\jdk\jfr\Category.html`

### Class Description

```java
@Target
(
TYPE
)

@Inherited

@Retention
(
RUNTIME
)
public @interface
Category
```

Event annotation, to associate the event type with a category, in the format
of a human-readable path.

The category determines how an event is presented to the user. Events that
are in the same category are typically displayed together in graphs and
trees. To avoid the overlap of durational events in graphical
representations, overlapping events must be in separate categories.

For example, to monitor image uploads to a web server with a separate thread
for each upload, an event called File Upload starts when the user uploads a
file and ends when the upload is complete. For advanced diagnostics about
image uploads, more detailed events are created (for example, Image Read,
Image Resize, and Image Write). During these detailed events. other low
level-events could occur (for example, Socket Read and File Write).

The following example shows a visualization that avoids overlaps:

```java
-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------
```

The example can be achieved by using the following categories:

Recording options and their purpose.

Event Name

Annotation

File Upload

@Category("Upload")

Image Read

@Category({"Upload", "Image Upload"})

Image Resize

@Category({"Upload", "Image Upload"})

Image Write

@Category({"Upload", "Image Upload"})

Socket Read

@Category("Java Application")

File Write

@Category("Java Application")

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String [] Returns the category names for this annotation, starting with the root.

---

### Additional Sections

#### Annotation Type Category

```java
@Target
(
TYPE
)

@Inherited

@Retention
(
RUNTIME
)
public @interface
Category
```

Event annotation, to associate the event type with a category, in the format
of a human-readable path.

The category determines how an event is presented to the user. Events that
are in the same category are typically displayed together in graphs and
trees. To avoid the overlap of durational events in graphical
representations, overlapping events must be in separate categories.

For example, to monitor image uploads to a web server with a separate thread
for each upload, an event called File Upload starts when the user uploads a
file and ends when the upload is complete. For advanced diagnostics about
image uploads, more detailed events are created (for example, Image Read,
Image Resize, and Image Write). During these detailed events. other low
level-events could occur (for example, Socket Read and File Write).

The following example shows a visualization that avoids overlaps:

```java
-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------
```

The example can be achieved by using the following categories:

Recording options and their purpose.

Event Name

Annotation

File Upload

@Category("Upload")

Image Read

@Category({"Upload", "Image Upload"})

Image Resize

@Category({"Upload", "Image Upload"})

Image Write

@Category({"Upload", "Image Upload"})

Socket Read

@Category("Java Application")

File Write

@Category("Java Application")

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

**Since:** 9

@Target

(

TYPE

)

@Inherited

@Retention

(

RUNTIME

)
public @interface

Category

Event annotation, to associate the event type with a category, in the format
of a human-readable path.

The category determines how an event is presented to the user. Events that
are in the same category are typically displayed together in graphs and
trees. To avoid the overlap of durational events in graphical
representations, overlapping events must be in separate categories.

For example, to monitor image uploads to a web server with a separate thread
for each upload, an event called File Upload starts when the user uploads a
file and ends when the upload is complete. For advanced diagnostics about
image uploads, more detailed events are created (for example, Image Read,
Image Resize, and Image Write). During these detailed events. other low
level-events could occur (for example, Socket Read and File Write).

The following example shows a visualization that avoids overlaps:

```java
-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------
```

The example can be achieved by using the following categories:

Recording options and their purpose.

Event Name

Annotation

File Upload

@Category("Upload")

Image Read

@Category({"Upload", "Image Upload"})

Image Resize

@Category({"Upload", "Image Upload"})

Image Write

@Category({"Upload", "Image Upload"})

Socket Read

@Category("Java Application")

File Write

@Category("Java Application")

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

The category determines how an event is presented to the user. Events that
are in the same category are typically displayed together in graphs and
trees. To avoid the overlap of durational events in graphical
representations, overlapping events must be in separate categories.

For example, to monitor image uploads to a web server with a separate thread
for each upload, an event called File Upload starts when the user uploads a
file and ends when the upload is complete. For advanced diagnostics about
image uploads, more detailed events are created (for example, Image Read,
Image Resize, and Image Write). During these detailed events. other low
level-events could occur (for example, Socket Read and File Write).

The following example shows a visualization that avoids overlaps:

```java
-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------
```

The example can be achieved by using the following categories:

Recording options and their purpose.

Event Name

Annotation

File Upload

@Category("Upload")

Image Read

@Category({"Upload", "Image Upload"})

Image Resize

@Category({"Upload", "Image Upload"})

Image Write

@Category({"Upload", "Image Upload"})

Socket Read

@Category("Java Application")

File Write

@Category("Java Application")

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

For example, to monitor image uploads to a web server with a separate thread
for each upload, an event called File Upload starts when the user uploads a
file and ends when the upload is complete. For advanced diagnostics about
image uploads, more detailed events are created (for example, Image Read,
Image Resize, and Image Write). During these detailed events. other low
level-events could occur (for example, Socket Read and File Write).

The following example shows a visualization that avoids overlaps:

```java
-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------
```

The example can be achieved by using the following categories:

Recording options and their purpose.

Event Name

Annotation

File Upload

@Category("Upload")

Image Read

@Category({"Upload", "Image Upload"})

Image Resize

@Category({"Upload", "Image Upload"})

Image Write

@Category({"Upload", "Image Upload"})

Socket Read

@Category("Java Application")

File Write

@Category("Java Application")

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

The following example shows a visualization that avoids overlaps:

```java
-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------
```

The example can be achieved by using the following categories:

Recording options and their purpose.

Event Name

Annotation

File Upload

@Category("Upload")

Image Read

@Category({"Upload", "Image Upload"})

Image Resize

@Category({"Upload", "Image Upload"})

Image Write

@Category({"Upload", "Image Upload"})

Socket Read

@Category("Java Application")

File Write

@Category("Java Application")

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

-------------------------------------------------------------------
| File Upload |
------------------------------------------------------------------
| Image Read | Image Resize | Image Write |
------------------------------------------------------------------
| Socket Read | Socket Read | | File Write |
-------------------------------------------------------------------

The File Upload, Image Read, and Socket Read events happen concurrently (in
the same thread), but the events are in different categories so they do not
overlap in the visualization.

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

The following examples shows how the category is used to determine how events
are visualized in a tree:

```java
|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write
```

|- Java Application
| |- Socket Read
| |- File Write
|- Upload
|- File Upload
|- Image Upload
|- Image Read
|- Image Resize
|- File Write

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

Returns the category names for this annotation, starting with the root.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

Returns the category names for this annotation, starting with the root.

---

#### Required Element Summary

Returns the category names for this annotation, starting with the root.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
[] value
```

Returns the category names for this annotation, starting with the root.

**Returns:** the category names

Element Detail

- value

```java
String
[] value
```

Returns the category names for this annotation, starting with the root.

**Returns:** the category names

---

#### Element Detail

value

```java
String
[] value
```

Returns the category names for this annotation, starting with the root.

**Returns:** the category names

---

#### value

String

[] value

Returns the category names for this annotation, starting with the root.

---

