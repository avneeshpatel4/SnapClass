import streamlit as st
from PIL import Image


@st.dialog("Capture or Upload Photos")
def add_photos_dialog():
    # Initialize session state variables
    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = []

    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"

    st.write("Add classroom photos to scan for attendance")

    # Tabs
    col1, col2 = st.columns(2)

    with col1:
        camera_type = (
            "primary"
            if st.session_state.photo_tab == "camera"
            else "tertiary"
        )

        if st.button("Camera", type=camera_type, use_container_width=True):
            st.session_state.photo_tab = "camera"
            st.rerun()

    with col2:
        upload_type = (
            "primary"
            if st.session_state.photo_tab == "upload"
            else "tertiary"
        )

        if st.button("Upload Photos", type=upload_type, use_container_width=True):
            st.session_state.photo_tab = "upload"
            st.rerun()

    # -------------------------
    # Camera
    # -------------------------
    if st.session_state.photo_tab == "camera":

        cam_photo = st.camera_input(
            "Take Snapshot",
            key="dialog_cam"
        )

        if cam_photo is not None:
            try:
                image = Image.open(cam_photo).convert("RGB")
                st.session_state.attendance_images.append(image)

                st.toast("Photo captured successfully.")
                st.rerun()

            except Exception as e:
                st.error(f"Unable to process image.\n\n{e}")

    # -------------------------
    # Upload
    # -------------------------
    elif st.session_state.photo_tab == "upload":

        uploaded_files = st.file_uploader(
            "Choose image files",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=True,
            key="dialog_upload",
        )

        if uploaded_files:

            added = 0

            for file in uploaded_files:
                try:
                    image = Image.open(file).convert("RGB")
                    st.session_state.attendance_images.append(image)
                    added += 1
                except Exception as e:
                    st.warning(f"Could not open {file.name}: {e}")

            if added > 0:
                st.toast(f"{added} photo(s) uploaded successfully.")
                st.rerun()

    st.divider()

    # Preview selected images
    if st.session_state.attendance_images:
        st.subheader("Selected Photos")

        cols = st.columns(3)

        for i, img in enumerate(st.session_state.attendance_images):
            with cols[i % 3]:
                st.image(
                    img,
                    use_container_width=True,
                    caption=f"Photo {i + 1}"
                )

    # Done button
    if st.button(
        "Done",
        type="primary",
        use_container_width=True,
    ):
        st.rerun()