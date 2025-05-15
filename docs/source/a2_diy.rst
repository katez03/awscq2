.. _a2_diy:

===
DIY
===

After completing the lab, the player does DIY by taking the following steps.

#. Start the DIY activity by selecting **DIY**.

   .. image:: pictures/0001-diy-A2.png
      :alt: Placeholder screenshot for A2 DIY Step 1 (Select DIY)
      :align: center
      :width: 600px

#. In the **DIY** interface, review the activity goals and validation method, then select **Open AWS Console**.

   .. image:: pictures/0002-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 2 (Read Goals and Open Console)
      :align: center
      :width: 600px

#. In **AWS Console**, locate and select the EC2 service.

   .. image:: pictures/0003-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 3 (Find and Select EC2 in Console)
      :align: center
      :width: 600px

#. Choose **Launch instance** to begin creating a new EC2 instance.

   .. image:: pictures/0004-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 4 (Select Launch Instance button)
      :align: center
      :width: 600px

#. Select the **Amazon Linux 2 AMI** from the list of available images.

   .. image:: pictures/0005-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 5 (Choose AMI)
      :align: center
      :width: 600px

#. Select the ``t2.micro`` Instance Type and proceed to **Next: Configure Instance Details**.

   .. image:: pictures/0006-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 6 (Choose Instance Type)
      :align: center
      :width: 600px

#. In the **Configure Instance Details**, select the appropriate **VPC** and **Subnet**, choosing a subnet different from the one used in the Practice lab.

   .. image:: pictures/0007-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 7 (Configure Instance Details - Subnet)
      :align: center
      :width: 600px

#. In **Advanced Details**, load the ``user-data`` file by selecting **As file**, then **Select file**, and proceed to **Next: Add Storage**.

   .. image:: pictures/0008-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 8 (Advanced Details - User Data)
      :align: center
      :width: 600px

#. Select **Next: Add Tags** from the Add Storage step.

   .. image:: pictures/0009-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 9 (Add Storage)
      :align: center
      :width: 600px

#. Proceed from Add Tags to **Next: Configure Security Group**.

   .. image:: pictures/00010-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 10 (Add Tags to Security Group)
      :align: center
      :width: 600px

#. In **Configure Security Group**, create a security group named ``Security-Group-Lab-2`` with description ``HTTP Group Lab 2``, adding an **HTTP** rule, then select **Review and Launch**.

   .. image:: pictures/00011-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 11 (Configure Security Group)
      :align: center
      :width: 600px

#. In **Review Instance Launch**, verify your settings and select **Launch**.

   .. image:: pictures/00012-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 12 (Review and Launch)
      :align: center
      :width: 600px

#. Select **Proceed without a key pair**, acknowledge the warning, and select **Launch Instances**.

   .. image:: pictures/00013-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 13 (Key Pair selection)
      :align: center
      :width: 600px

#. View your newly launched instances by selecting **View Instances**.

   .. image:: pictures/00014-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 14 (View Instances)
      :align: center
      :width: 600px

#. After creating two EC2 instances, copy the **Instance ID** for both.

   .. image:: pictures/00015-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 15 (Copy Instance IDs)
      :align: center
      :width: 600px

#. Paste the Instance ID from the first Availability Zone (AZ1) into the validation form.

   .. image:: pictures/00016-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 16 (Paste ID in AZ1)
      :align: center
      :width: 600px

#. Paste the Instance ID from the second Availability Zone (AZ2) into the validation form.

   .. image:: pictures/00017-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 17 (Paste ID in AZ2)
      :align: center
      :width: 600px

#. Select **VALIDATE** to check your solution.

   .. image:: pictures/00018-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 18 (Select VALIDATE)
      :align: center
      :width: 600px

#. Confirm that the **VALIDATION MESSAGE** indicates "Success! …" after validating.

   .. image:: pictures/00019-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 19 (Validation Success message)
      :align: center
      :width: 600px

#. Select **EXIT** to close the validation interface.

   .. image:: pictures/00020-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 20 (Select EXIT)
      :align: center
      :width: 600px

#. In the **ASSIGNMENT** interface, select **COLLECT** to claim your rewards.

   .. image:: pictures/00021-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 21 (Collect Rewards)
      :align: center
      :width: 600px

#. You have successfully completed the DIY activity and received your rewards.

   .. image:: pictures/00022-diy.png
      :alt: Placeholder screenshot for A2 DIY Step 22 (Get rewarded - final step)
      :align: center
      :width: 600px
