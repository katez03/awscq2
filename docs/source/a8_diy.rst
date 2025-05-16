.. _a8_diy:

===
DIY
===

After completing the lab, the player does DIY.

Here’s the full set of steps:

#. In the **AWS Console** interface:

   * Find **IAM**.
   * Select **IAM**.

   .. image:: pictures/0001-diy-A8.png
      :alt: AWS console showing IAM service.
      :align: center
      :width: 600px

#. In the **IAM** interface:

   * Select **User groups**.
   * Select the **SupportEngineers** group.
   * Select **Permissions**.

   .. image:: pictures/0002-diy-A8.png
      :alt: IAM user groups interface showing SupportEngineers selected and Permissions tab.
      :align: center
      :width: 600px

#. In the **IAM** interface (Permissions):

   * Find **AmazonEC2ReadOnlyAccess** (the policy attached to the group).
   * Select **AmazonEC2ReadOnlyAccess**.

   .. image:: pictures/0003-diy-A8.png
      :alt: IAM group permissions showing AmazonEC2ReadOnlyAccess policy found and selected.
      :align: center
      :width: 600px

#. In the **IAM** interface (Permissions):

   * Select **Add permissions**.

   .. image:: pictures/0004-diy-A8.png
      :alt: IAM group permissions interface showing Add permissions button.
      :align: center
      :width: 600px

#. In the **Add permissions** interface:

   * Under **Add permissions**, select **Attach policies**.

   .. image:: pictures/0005-diy-A8.png
      :alt: IAM Add permissions interface showing Attach policies option.
      :align: center
      :width: 600px

#. In the **IAM** interface (Attach policies):

   * Find **RDSReadOnlyAccess**.
   * Select **AmazonRDSReadOnlyAccess**.

   .. image:: pictures/0006-diy-A8.png
      :alt: IAM Attach policies interface showing search for and selection of RDSReadOnlyAccess.
      :align: center
      :width: 600px

#. In the **IAM** interface (Attach policies):

   * Select **Add permissions** (to attach the selected policy).

   .. image:: pictures/0007-diy-A8.png
      :alt: IAM Attach policies interface showing Add permissions button to finalize attachment.
      :align: center
      :width: 600px

#. In the **IAM** interface:

   * Select **User groups**.
   * Select **Permissions**.
   * View the **Policy name** list (it should now include RDSReadOnlyAccess).

   .. image:: pictures/0008-diy-A8.png
      :alt: IAM user groups interface showing Permissions tab with updated policy list.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * Enter **SupportEngineers** (the user group name).
   * Select **VALIDATE**.

   .. image:: pictures/0009-diy-A8.png
      :alt: DIY interface showing user group name entry and Validate button.
      :align: center
      :width: 600px

#. In the **DIY** interface:

   * After selecting **VALIDATE**, the **VALIDATION MESSAGE** appears.
   * View the message “**You have granted the correct permissions…**”.
   * Select **EXIT** to exit.

   .. image:: pictures/00010-diy-A8.png
      :alt: DIY interface showing validation success message.
      :align: center
      :width: 600px

#. After returning to the city interface:

   * Select **ASSIGNMENT**.
   * Select **COLLECT**.
   * Select **NEXT**.
   * Select **COLLECT**.
   * Congratulations to the award winning player!

   .. image:: pictures/00011-diy-A8.png
      :alt: City interface showing assignment collection and final congratulations.
      :align: center
      :width: 600px
